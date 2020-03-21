#!python3
'''
This script xxx. 


Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
import re


def get_dics(filename):
	dics = []
	f = open(filename,'r',encoding='utf-8')
	r = re.compile(r'^([^\t]*?)\t+(.+?)\s*$')
	for line in f:
		m = r.match(line)
		if not m:
			continue

		title = m.group(1)
		desc = m.group(2)
		if not title: 
			continue
			
		dic = {'title': title, 'desc': desc}
		dics.append(dic)

	f.close()
	return dics
	
			
def main():
	if not keyboard.is_keyboard():
		return

	dics = get_dics('Snippet Regular Expression.txt')
	
	items = [d['title'] + '  ' + d['desc'] for d in dics]
	selected_item = dialogs.list_dialog('select', items)
	if not selected_item:
		return

	idx = items.index(selected_item)

	new_text = dics[idx]['title']
	keyboard.insert_text(new_text)


if __name__ == '__main__':
	main()

