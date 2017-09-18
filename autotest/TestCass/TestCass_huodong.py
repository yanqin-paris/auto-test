# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.GetTestDataPath import GetTestDataPath
from PublicTools.globalpy import GLOBAL_token

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_get_huoqupingtuanhuodngxiangqing():
    for i in range(3, 5):
        table = Testdata.sheets()[4]  # 选择excle表中的sheet
        if i == 4:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "id": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "4-1-" + str(i + 1)
        htestcassname = "【活动模块】 获取拼团活动详情 (m站)" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'activity/team-buying', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqupingtuanhuodngxiangqing()
