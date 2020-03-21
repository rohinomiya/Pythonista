#!python3
'''
This script deletes right letter.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs


def main():
	if not keyboard.is_keyboard():
		return

	keyboard.move_cursor(1)
	keyboard.backspace(1)

if __name__ == '__main__':
	main()

