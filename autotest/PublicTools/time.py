# coding:UTF-8
import time


def shijiancuo(daydelta):
    dt = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 86400 * daydelta))
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return str(int(timestamp))

'''
print(shijiancuo(2))
print(shijiancuo(30))
print(shijiancuo(34))
'''
