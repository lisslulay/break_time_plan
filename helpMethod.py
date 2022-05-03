import time


""" Current data
"""
def currentData() -> str:
    return time.strftime("%m-%d", time.localtime())

