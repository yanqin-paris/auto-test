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
# print(GetTestDataPath())
# print(GetTestReportPath())
# print(GetTestConfigPath())
