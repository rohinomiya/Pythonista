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

	selected_text = keyboard.get_selected_text()
	if selected_text:
		keyboard.backspace(1)

	tpl = keyboard.get_input_context()
	left = tpl[0]
	delete_count = len(left)

	keyboard.backspace(delete_count)


if __name__ == '__main__':
	main()

