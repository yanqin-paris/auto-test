# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim

'''
# 导入测试用例
import time
import TestCass.TestCass_tongyong
import TestCass.TestCass_yonghu
from PublicTools.log import logger


def TestCass_tongyong_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_tongyong.test_get_banbengengxin()
    TestCass.TestCass_tongyong.test_get_huodongzige()
    TestCass.TestCass_tongyong.test_get_jianchashoujihao()
    logger.info("结束测试")


def TestCass_yonghu_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_yonghu.test_post_duanxindenglu()
    TestCass.TestCass_yonghu.test_post_mimadenglu()
    TestCass.TestCass_tongyong.test_get_jianchashoujihao()
    logger.info("结束测试")