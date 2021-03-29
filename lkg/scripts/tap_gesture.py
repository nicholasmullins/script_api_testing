import logging

log = logging.getLogger(__name__)

def run(context):
    context.perform_gesture('tap', 'lnk_logout')
