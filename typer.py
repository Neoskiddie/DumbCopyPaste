from pynput.keyboard import Key, Controller
import argparse
import time

# Parser setup
parser = argparse.ArgumentParser(description='Type all lines of a file as one long line. Made to copy whole base64 encoded file to a VM that was only accessible through browser.')

parser.add_argument('-s', '--sleep', type=int, default=3, help='time to sleep before typing')
parser.add_argument('-l', '--letter_break', type=float, default=0.05, help='time to sleep between letters')
parser.add_argument('-b', '--breaks', type=float, default=0.05, help='time to sleep between lines')
parser.add_argument('file', type=str, help='file to use')

args = parser.parse_args()

keyboard = Controller()
print(f"Sleeping for {args.sleep} seconds and executing")
time.sleep(args.sleep)

def type_character(character):
    # Check if character is uppercase or requires shift
    if character.isupper() or character in '~!@#$%^&*()_+{}|:"<>?':
        with keyboard.pressed(Key.shift):
            keyboard.press(character.lower() if character.isupper() else character)
            keyboard.release(character.lower() if character.isupper() else character)
    else:
        keyboard.press(character)
        keyboard.release(character)

with open(args.file) as infile:
    for line in infile:
        for char in line.rstrip():
            type_character(char)
            time.sleep(args.letter_break)
        time.sleep(args.breaks)
