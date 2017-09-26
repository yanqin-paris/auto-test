# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim

'''
import os


def GetTestDataPath():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\TestData\\TestData.xls'


def GetTestData():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\TestData\\'


def GetTestReportPath():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\TestReport\\'


def GetTestConfigPath():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) + '\\config\\'


def GetTestLogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join("logs", "log.txt")
# return os.path.dirname(os.path.dirname(os.path.abspath(__file__))) +
# '\\logs\\log.txt'
# print(os.path.abspath(__file__))
# print(GetTestLogPath())
# print(GetTestDataPath())
# print(GetTestReportPath())
# print(GetTestConfigPath())
# print(os.path.dirname(os.getcwd()))


def GetLogConfigPath():
    return os.path.join(os.path.dirname(os.getcwd()), "config", "logconfig.conf")
# print(GetLogConfigPath())
# print(GetTestConfigPath())
