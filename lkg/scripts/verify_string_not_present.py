import logging


def run(context):
        context.verify(grep="first-born child", grep_count=0)
        context.perform_gesture('tap', 'btn_verified')