#!python3
'''
This script cuts the word on cursor to clipboard.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
import re
import clipboard


def delete_selection():
	selected_text = keyboard.get_selected_text()
	if selected_text:
		keyboard.backspace(1)
	return


def move_to_first_letter_of_word():
	left, right = keyboard.get_input_context()
	if not left:
		return

	m = re.match(r'.*\b([^ ]+?)$', left)
	if not m:
		return

	left_word = m.groups()[0]
	count = len(left_word)
	keyboard.move_cursor(-count)
	return


def cut_word():
	left, right = keyboard.get_input_context()
	if not right:
		return

	m = re.match(r'^(.+?\b *)', right)
	if not m:
		return

	right_word = m.groups()[0]
	count = len(right_word)

	keyboard.move_cursor(count)
	keyboard.backspace(count)
	
	clipboard.set(right_word)
	return


def main():
	if not keyboard.is_keyboard():
		return

	delete_selection()
	move_to_first_letter_of_word()
	cut_word()


if __name__ == '__main__':
	main()
