import time


def get_current_time():
    return time.strftime("%d/%h/%Y %H:%M:%S", time.localtime(time.time()))

