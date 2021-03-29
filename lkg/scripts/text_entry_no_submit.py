import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry_no_submit', 'inp_email','publicbot@appdiff.com')
