#!python3
'''
This script surrounds selected text with other text selected from menu. 

Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
import re


def get_dics(filename):
	dics = []
	f = open(filename, "r", encoding="utf-8")
	if not f:
		return dics
		
	for line in f:
		if not line:
			continue

		dics.append(line)

	f.close()
	return dics


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	snippets = get_dics('Surround Text.txt')
	selected = dialogs.list_dialog('select Replacements', snippets)
	if not selected:
		return

	m = re.match(r'^(.*)〜(.*)$', selected)
	if not m:
		return

	g = m.groups()
	left = g[0]
	right = g[1]
	newText = left + text + right
	keyboard.insert_text(newText)


if __name__ == '__main__':
	main()

