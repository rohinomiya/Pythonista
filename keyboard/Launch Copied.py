#!python3
'''
This script launches Copied App.

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
import webbrowser


def main():
	if not keyboard.is_keyboard():
		return

	url = 'copied://'
	webbrowser.open(url)


if __name__ == '__main__':
	main()

