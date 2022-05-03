from const import *
from helpMethod import *
import time as localtime

""" Add a line in log
    [05-03]: +15min<desc> 14:22\n

"""
def addLineInLog(time: int, desc: str):
    ## read
    f = open(LOD_FILE, 'r')
    data = f.readlines()
    f.close()   
    ## write
    entry = "[" + currentData() + "]: +" + str(time) + "min<" + desc + "> "\
            + localtime.strftime("%H:%M", localtime.localtime()) + "\n"
    print(entry, end="")
    data.append(entry)
    f = open(LOD_FILE, 'w')
    f.writelines(data)
    f.close()


""" Add a line in log
    [05-03]:0 -> 195min

"""
def addChangeInLog(date: str, oldTime: int, newTime: int):
    ## read
    f = open(LOD_FILE, 'r')
    data = f.readlines()
    f.close()   
    ## write
    if oldTime == None:
        oldTime = 0
    entry = "[" + currentData() + "]: " + str(oldTime) + " -> " \
            + str(newTime) + "min\n"
    print(entry, end="")
    data.append(entry)
    f = open(LOD_FILE, 'w')
    f.writelines(data)
    f.close()
