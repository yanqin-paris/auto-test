# -*- coding:utf-8 -*-

'''
Created on 2017年9月1日

@author: Jim

'''
import json
import requests
import xlrd
import sys
from PublicTools.log import logger
from PublicTools.GetTestDataPath import GetTestDataPath
from PublicTools.GetTestDataPath import GetDbConfigPath
from PublicTools.GetTestDataPath import Writeconfig
from PublicTools.mydb import MyDB

Writeconfig(sys.argv[1])

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
user_id = table.cell(10, 1).value
db = table.cell(13, 1).value


def test_get_token():
    query = "SELECT access_token FROM `user` where id = %s"
    testdb = MyDB(GetDbConfigPath(), db)
    data = (user_id)
    r = testdb.select_one_record(query, data)
    access_token = r['access_token']
    logger.info('当前token为：' + access_token)
    return access_token
