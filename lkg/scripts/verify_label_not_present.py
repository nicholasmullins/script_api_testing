'''
This script verifies a label is not present on the screen.
This is useful if you expect an element to have been removed.
Replace <your_label> below with the label name you gave your element in the test.ai GUI.
'''

import logging

log = logging.getLogger(__name__)

def run(context):
    context.verify(labels=["btn_accept"], label_count=0)
    context.perform_gesture('tap', 'btn_verified')