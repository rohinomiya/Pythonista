#!python3
'''
This script transform selected text like below:
beforep
	Pythonista3 is 
	amazing!!	
after:
	＿人人人人人人人人人＿
	＞　Pythonista3 is 　＜
	＞　amazing!!　　　　＜
	￣Y^Y^Y^Y^Y^Y^Y^Y^Y^Y￣
	
Note: This script is designed for the Pythonista Keyboard. You can enable it in the Settings app (under General > Keyboard > Keyboards > Add New Keyboard...). Please check the documentation for more information.
'''

import keyboard
import dialogs
import unicodedata
import math


def zenhanlen(s):
	sum = 0
	hankakuTypes = ['H', 'Na']
	for c in s:
		type = unicodedata.east_asian_width(c)
		clen = 1 if type in hankakuTypes else 2
		sum += clen
	return sum


def stringByBytes(s, byteLen):
	s2 = s * (byteLen * 2)
	while byteLen < zenhanlen(s2):
		s2 = s2[0:len(s2) - 1]
	return s2


def stringByBytes2(s, byteLen):
	hanSpaceCount = byteLen - zenhanlen(s)
	zenSpaceCount = math.floor(hanSpaceCount / 2)
	extraCount = hanSpaceCount % 2
	s2 = s + '　' * zenSpaceCount + ' ' * extraCount
	while byteLen < zenhanlen(s2):
		s2 = s2[0:len(s2) - 1]
	return s2


def suddendeath(s):
	width = 0
	lines = s.splitlines()
	height = len(lines)
	for line in lines:
		lineWidth = zenhanlen(line)
		width = max(width, lineWidth)
	# 左右に全角スペース1個分の余白を用意
	width += 4

	newLines = []
	newLines.append('＿' + stringByBytes('人', width) + '＿')
	for line in lines:
		newLines.append('＞' + stringByBytes2('　' + line + '　', width) + '＜')
	newLines.append('￣' + stringByBytes('Y^', width) + '￣')
	new_s = '\n'.join(newLines)

	return new_s


def main():
	if not keyboard.is_keyboard():
		return

	text = keyboard.get_selected_text()

	if not text:
		dialogs.hud_alert('No text selected', 'error')
		return

	newText = suddendeath(text)
	keyboard.insert_text(newText)


if __name__ == '__main__':
	main()

