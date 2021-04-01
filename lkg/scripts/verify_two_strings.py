import logging


def run(context):
        context.verify(grep="No Place Like", grep_count=2)
        context.perform_gesture('tap', 'btn_verified')