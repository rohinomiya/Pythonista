#!python3
'''
This script cuts selected text to clipboard.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import clipboard


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	clipboard.set(text)
	if text:
		# clear selection
		keyboard.insert_text(' ')
		keyboard.backspace(1)


if __name__ == '__main__':
	main()
