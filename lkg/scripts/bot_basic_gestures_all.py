import logging
import time

log = logging.getLogger(__name__)

def run(context):

	context.perform_gesture('tap', 'btn_tap')
	context.perform_gesture('double_tap', 'btn_double_tap')	

	context.perform_gesture('swipe_up', '')
	context.perform_gesture('swipe_down', '')	
	
	context.perform_gesture('text_entry_no_submit', 'inp_text_entry_no_submit', 'Bot Gestures All Script Text')
	context.perform_gesture('text_entry', 'inp_text_entry', 'Completed!!')