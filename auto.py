import librosa
import numpy as np
import pydub

# Define the frequency of each note in the piano scale
piano_scale = {
    "C": 261.63,
    "C#": 277.18,
    "D": 293.66,
    "D#": 311.13,
    "E": 329.63,
    "F": 349.23,
    "F#": 369.99,
    "G": 392.00,
    "G#": 415.30,
    "A": 440.00,
    "A#": 466.16,
    "B": 493.88
}

# Function to find the closest note in the piano scale for a given frequency
# Function to find the closest note in the piano scale for a given frequency
# Function to find the closest note in the piano scale for a given frequency
def find_closest_note_frequency(frequency):
    closest_note = []
    
    for freq in frequency:
        note_differences = [abs(piano_scale[note] - freq) for note in piano_scale]
        closest_note_index = np.argmin(note_differences)
        closest_note.append(list(piano_scale.values())[closest_note_index])
    
    return np.array(closest_note)



# Function to autotune an audio file
def autotune_audio(input_file, output_file):
    # Load the audio file
    audio, sr = librosa.load(input_file)

    # Detect pitch and compute corresponding note frequencies
    pitches, magnitudes = librosa.piptrack(y=audio, sr=sr)
    note_frequencies = [find_closest_note_frequency(pitch) for pitch in pitches]

    # Convert note frequencies to pitch shifts
    target_pitches = [librosa.note_to_midi(note) for note in note_frequencies]
    pitch_shifts = target_pitches - pitches

    # Calculate the median pitch shift value
    median_pitch_shift = np.median(pitch_shifts).item()

    # Apply pitch correction to the audio
    corrected_audio = librosa.effects.pitch_shift(audio, sr, n_steps=median_pitch_shift)

    # Save the autotuned audio as an MP3 file
    pydub.AudioSegment(
        corrected_audio.astype(np.float32),
        frame_rate=sr,
        sample_width=4,
        channels=1
    ).export(output_file, format="mp3")

    print("Autotuning complete. Output saved as", output_file)

# Usage example
input_file = "voice-message.mp3"  # Replace with your input audio file (MP3 format)
output_file = "output.mp3"  # Specify the output file name (MP3 format)
autotune_audio(input_file, output_file)
