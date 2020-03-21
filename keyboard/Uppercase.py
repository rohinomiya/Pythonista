#!python3
'''
This script converts selected text to uppercase.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	new_text = text.upper()
	keyboard.insert_text(new_text)


if __name__ == '__main__':
	main()

