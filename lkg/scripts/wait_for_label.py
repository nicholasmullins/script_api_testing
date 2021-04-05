import logging
import time

def run(context):

    def wait_for_label():
        context.perform_gesture('tap', 'btn_wait_for_label')


    context.wait(wait_for_label, 5, sleep_in_between=5)    

