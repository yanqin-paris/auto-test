# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim

'''
import os
import time
import configparser


def GetenvironmentPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "environment.conf")


def Writeconfig(e):
    environmentPath = GetenvironmentPath()
    config = configparser.ConfigParser()
    config.read(GetenvironmentPath())
    config.set('environment', 'environment', e)
    cfgfile = open(environmentPath, "w")
    config.write(cfgfile)
    cfgfile.close()
    print('写入成功：' + e)


def GetTestDataPath():
    config = configparser.ConfigParser()
    config.read(GetenvironmentPath())
    environment = config['environment']['environment']
    if environment == "test":
        ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(ospath, "TestData", "TestDatatest.xls")
    elif environment == "auto":
        ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        return os.path.join(ospath, "TestData", "TestData.xls")


def GetLogoDataPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "TestData", "logo.png")


def GetTestReportPath():
    now = time.strftime("%Y-%m-%d-%H-%M-%S-", time.localtime(time.time()))
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "TestReport", now + "report.xlsx")


def GetDbConfigPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "dbconfig.conf")


def GetMailConfigPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "mail.conf")


def GetTestLogPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "logs", "log.txt")


def GetLogConfigPath():
    ospath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(ospath, "config", "logconfig.conf")
