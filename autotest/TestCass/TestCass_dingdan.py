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


def test_post_pingtuankadancigoumai():
    for i in range(3, 5):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
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
        htestcassname = "订单模块拼团卡单次购买 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'order/single-buy', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_post_pingtuankadancigoumai()


def test_post_kaituanmzhan():
    for i in range(13, 15):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 14:
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
        htestcassid = "3-2-" + str(i + 1)
        htestcassname = "订单模块开团 m站" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'order/initiate-activities', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_kaituanmzhan()


def test_post_cantuanmzhan():
    for i in range(21, 23):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 22:
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
        htestcassid = "3-3-" + str(i + 1)
        htestcassname = "订单模块参团 m站" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/participate-activities', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_cantuanmzhan()


def test_post_changjianyajinrenzhengdingdan():
    for i in range(31, 35):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 33:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "channel": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "channel": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-4-" + str(i + 1)
        htestcassname = "订单模块创建押金认证订单 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/deposit-certificate', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_changjianyajinrenzhengdingdan()


def test_get_xuanzeyouhuiquan():
    for i in range(39, 41):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "price": table.cell(i, 1).value,
            "type": table.cell(i, 2).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-5-" + str(i + 1)
        htestcassname = "订单模块选择优惠券 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestGetRequest(hurl + 'order/user-coupon', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_xuanzeyouhuiquan()
