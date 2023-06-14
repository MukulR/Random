import openai

# Set up your OpenAI API credentials
openai.api_key = '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'

# Define the conversation history
conversation = [
    {'role': 'system', 'content': 'You are a helpful assistant.'},
    {'role': 'user', 'content': 'Who won the world series in 2020?'}
]

# Generate a response from ChatGPT
response = openai.Completion.create(
    engine='text-davinci-003',
    prompt=conversation,
    max_tokens=50
)

# Extract and print the generated reply
reply = response.choices[0].text.strip()
print('ChatGPT: ' + reply)


