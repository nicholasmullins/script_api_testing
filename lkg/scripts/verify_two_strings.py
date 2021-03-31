import logging


def run(context):
        context.verify(grep="No Place Like Home", grep_count=2)
        context.perform_gesture('tap', 'btn_verified')