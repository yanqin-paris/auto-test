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

from PublicTools.globalpy import GLOBAL_TestDataPath

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_get_huoquzhuantiguanlibiao():
    for i in range(3, 6):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        hdata = {
            "platform": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "5-1-" + str(i + 1)
        htestcassname = "首页获取专题馆列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'home/topics', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquzhuantiguanlibiao()


def test_get_peizhiwenjiangengxin():
    for i in range(13, 14):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "5-2-" + str(i + 1)
        htestcassname = "首页获取场合列表 V1 " + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'home/occasion', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_peizhiwenjiangengxin()


def test_get_huoqushouyeshuju():
    for i in range(21, 24):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        hdata = {
            "platform": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "5-3-" + str(i + 1)
        htestcassname = "首页获取首页数据 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'home', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_huoqushouyeshuju()


def test_get_huoqupingpaixiangqing():
    for i in range(31, 34):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        hdata = {
            "id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "5-4-" + str(i + 1)
        htestcassname = "品牌获取品牌详情 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'brand', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_huoqupingpaixiangqing()


def test_get_huoqupingpaiguanshouye():
    for i in range(39, 40):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "5-5-" + str(i + 1)
        htestcassname = "品牌获取品牌馆首页 V1 " + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'brand/home', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_huoqupingpaiguanshouye()

'''
def test_post_pingtuankadancigoumai2():
    for i in range(3, 6):
        table = Testdata.sheets()[5]  # 选择excle表中的sheet
        if i == 4:
            hdata = {
                "access_token": table.cell(i, 0).value
            }

        else:
            hdata = {
                "access_token": access_token
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-1-" + str(i + 1)
        htestcassname = "【订单模块】拼团卡单次购买 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'order/single-buy', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
'''
