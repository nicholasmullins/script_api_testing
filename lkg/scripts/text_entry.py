import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('text_entry', 'inp_password','mypassword')
