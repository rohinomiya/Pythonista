#!python3
'''
This script pastes text from clipboard.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import clipboard


def main():
	if not keyboard.is_keyboard():
		return

	text = clipboard.get()
	if not text:
		return

	keyboard.insert_text(text)


if __name__ == '__main__':
	main()

