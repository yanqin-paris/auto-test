# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim

'''
import os
import time


def GetTestDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "TestData", "TestData.xls")
# return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
# '\\TestData\\TestData.xls'


def GetLogoDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "TestData", "logo.png")


def GetTestReportPath():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "TestReport", now + "report.xlsx")
# return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
# '\\TestReport\\'


def GetDbConfigPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "dbconfig.conf")
# return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
# '\\config\\'


def GetMailConfigPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "mail.conf")


def GetTestLogPath():
    return os.path.join(os.getcwd(), "autotest", "logs", "log.txt")
# return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
# '\\logs\\log.txt'
# print(os.path.abspath(__file__))
# print(GetTestLogPath())
# print(GetTestDataPath())
# print(GetTestReportPath())
# print(GetTestConfigPath())
# print(os.path.dirname(os.getcwd()))


def GetLogConfigPath():
    return os.path.join(os.getcwd(), "autotest", "config", "logconfig.conf")
print(GetLogConfigPath())
print(GetTestLogPath())
# print(GetTestConfigPath())
