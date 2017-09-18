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


def test_get_lingquyouhuiquan():
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
# test_post_lingquyouhuiquan()


def test_get_huiyuanzhongxinshouyeshuju():
    for i in range(31, 34):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 32 or i == 33:
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
        htestcassid = "2-4-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 会员中心首页数据V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/member-centre', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huiyuanzhongxinshouyeshuju()


def test_post_xiugaimima():
    for i in range(39, 44):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 42:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "old_password": table.cell(i, 1).value,
                "password": table.cell(i, 2).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "old_password": table.cell(i, 1).value,
                "password": table.cell(i, 2).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-5-" + str(i + 1)
        htestcassname = "【用户模块】 修改密码 V1 " + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'user/password', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_xiugaimima()


def test_get_quanbuhuiyuantequan():
    for i in range(49, 51):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 50:
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
        htestcassid = "2-6-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 全部会员特权V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/member-privilege', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_quanbuhuiyuantequan()


def test_post_fenxiangmeiyijianglijifen():
    for i in range(57, 60):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 58 or i == 59:
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
        htestcassid = "2-6-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 全部会员特权V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'user/share-success', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_fenxiangmeiyijianglijifen()


def test_get_wodenvshenkadingdan():
    for i in range(65, 68):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 66 or i == 67:
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
        htestcassid = "2-7-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单 V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/card-orders', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdan()


def test_get_wodenvshenkadingdan2():
    for i in range(71, 74):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 72 or i == 73:
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
        htestcassid = "2-8-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单 V1-3.2.0 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/lteration-card-orders', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdan2()


def test_get_wodenvshenkadingdanxiangqing():
    for i in range(77, 80):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 78:
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
        htestcassid = "2-9-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单详情 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/card-order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdanxiangqing()
