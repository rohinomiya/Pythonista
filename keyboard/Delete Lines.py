#!python3
'''
This script deletes.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard


def delete_selection():
	selected_text = keyboard.get_selected_text()
	if selected_text:
		keyboard.insert_text(' ')
		keyboard.backspace(1)
	return


def move_to_first_letter_of_line():
	left, right = keyboard.get_input_context()
	# if column == 0, returns '\n'
	if not left or left == '\n':
		return

	count = len(left)
	keyboard.move_cursor(-count)
	return


def delete_line():
	left, right = keyboard.get_input_context()
	count = len(right + '\n')
	keyboard.move_cursor(count)
	keyboard.backspace(count)
	return


def main():
	if not keyboard.is_keyboard():
		return

	delete_selection()
	move_to_first_letter_of_line()
	delete_line()


if __name__ == '__main__':
	main()

