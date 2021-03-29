import logging
import time

log = logging.getLogger(__name__)

def run(context):

	context.find_element('lnk_posts')
    	context.perform_gesture('tap', 'lnk_logout')

	context.perform_gesture('text_entry_no_submit', 'inp_email', 'publicbot@appdiff.com')
	context.perform_gesture('text_entry', 'inp_password', 'mypassword')
	
	context.perform_gesture('swipe_up', '')
	context.perform_gesture('swipe_down', '')

	# context.perform_gesture_on_coord('swipe_custom', {'start_x': 0, 'start_y': 0, 'end_x': 200, 'end_y': 200, 'duration': 2000})  - CUSTOM SWIPING NOT YET SUPPORTED ON WEB

	context.perform_gesture('double_tap', 'mnu_profile')
	
