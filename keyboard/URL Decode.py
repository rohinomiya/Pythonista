#!python3
'''
This script transforms selected text to URL decoded.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
from urllib.parse import unquote


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	newText = unquote(text)
	keyboard.insert_text(newText)


if __name__ == '__main__':
	main()

