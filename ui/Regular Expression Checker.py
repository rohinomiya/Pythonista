import ui
import re
import console
import clipboard
import dialogs


def on_insert_re(sender):
	tableview1.hidden = not tableview1.hidden


def on_select_re(sender):
	# todo: 不要になればハズせ
	tableview1.hidden = True
	
	
	selected = sender.items[sender.selected_row]
	# todo: 置き換えではなくカーソル位置挿入にして
	text_re.text = selected


def on_copy_re(sender):
	clipboard.set(text_re.text)

	dialogs.hud_alert('Copied.', 'success')


def on_paste_any_text(sender):
	text_any = sender.superview['text_any']
	text_any.text = clipboard.get()


def onCheck(sender):
	text_result.text = text_re.text + text_any.text

	try:
		#r = re.compile(text_re.text)
		m = re.match(text_re.text, text_any.text)
		if not m:
			return

		lines = []
		g = m.groups()

		for index, item in enumerate(g):
			lines.append(f'groups[{index}]="{item}"')

		text_result.text = '\n'.join(lines)
	except Exception as e:
		text_result.text = e.args[0]


v = ui.load_view()

text_re = v['text_re']
text_any = v['text_any']
text_result = v['text_result']
tableview1 = v['tableview1']
tableview1.hidden = True

v.present('sheet')

