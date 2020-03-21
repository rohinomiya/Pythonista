#!python3
'''
This script.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
from urllib.parse import quote
import shortcuts
import webbrowser


def main():

	text = '万徳'

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	newText = quote(text, safe=':/')

	# todo: 
	url = f'quicka2://?text={newText}'
	#url = f'quicka2://?text=aaa'
	shortcuts.open_url(url)
	#.open()

if __name__ == '__main__':
	main()

