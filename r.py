from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
time.sleep(3)

delay = 0.01  # 10ms delay

for letter in range(ord('a'), ord('z') + 1):
    key = chr(letter)
    keyboard.press(key)
    keyboard.release(key)
    time.sleep(delay)
