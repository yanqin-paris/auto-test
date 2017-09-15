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


def test_post_mimadenglu():
    for i in range(3, 6):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        hdata = {
            "mobile": table.cell(i, 0).value,
            "password": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-1-" + str(i + 1)
        htestcassname = "【用户模块】 密码登录 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/password-login', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_post_mimadenglu()


def test_post_duanxindenglu():
    for i in range(13, 16):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        hdata = {
            "mobile": table.cell(i, 0).value,
            "code": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type,
            'token': htoken
        }
        htestcassid = "2-2-" + str(i + 1)
        htestcassname = "【用户模块】 会员登录 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/login', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_duanxindenglu()


def test_post_lingquyouhuiquan():
    for i in range(21, 26):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 25:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "type": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "type": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-3-" + str(i + 1)
        htestcassname = "【优惠券模块】 ​ 领取优惠券 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'coupon/receive', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
test_post_lingquyouhuiquan()
