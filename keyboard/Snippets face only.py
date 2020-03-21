#!python3
'''
This shows a simple list of text replacements you've defined in the system-wide keyboard settings (Settings app).

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs


def main():
	if not keyboard.is_keyboard():
		print('This script is meant to be run in the Pythonista keyboard.')
		return

	# (phrase, shortcut)
	all = keyboard.get_text_replacements()
	snippets = [s[0] for s in all if s[1] == '☻']
	snippets.sort()

	if len(snippets) == 0:
		dialogs.hud_alert('No Text Replacements')
		return

	selected = dialogs.list_dialog('Text Replacements', snippets)
	if selected:
		keyboard.insert_text(selected)


if __name__ == '__main__':
	main()
 
