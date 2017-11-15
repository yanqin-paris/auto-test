# coding:UTF-8
import time


def shijiancuo(daydelta):
    dt = time.strftime(
        "%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 86400 * daydelta))
    timeArray = time.strptime(dt, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return str(int(timestamp))


def shijiancuobagtime(daydelta, shijian):
    dt = time.strftime(
        "%Y-%m-%d", time.localtime(time.time() + 86400 * daydelta))
    dt1 = dt + " " + shijian
    timeArray = time.strptime(dt1, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(timeArray)
    return str(int(timestamp))

#print(shijiancuobagtime(1, "16:00:00"))
#print(shijiancuobagtime(1, "17:00:00"))
