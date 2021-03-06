# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''


import threading  # 导入多线程库
import TestAllCass


def hthreads():
    threads = []  # 创建线程数组
    # 定义线程
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_dingdangoumai_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_tongyong_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_yonghu_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_huodong_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_dingdan_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_shouye_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_shangpin_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_yuyue_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_nvshenka_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_faxian_Cass()))  # 添加线程到数组
    threads.append(
        threading.Thread(target=TestAllCass.TestCass_zulinjihua_Cass()))  # 添加线程到数组

    for h in threads:
        # 读取数组里的所有线程，并同时执行
        h.start()  # 开始线程活动
        h.join()  # 把主线程挂起，等待上面的线程跑完了再运行
