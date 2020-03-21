#!python3
'''
This script launches quicka2 with selected text.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
from urllib.parse import quote
import webbrowser


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	newText = quote(text, safe=':/')
	url = f'quicka2://?text={newText}'
	
	#shortcuts.open_url(url) 
	webbrowser.open(url)

if __name__ == '__main__':
	main()
