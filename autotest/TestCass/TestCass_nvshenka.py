# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.TestRequest import TestDeleteRequest
from PublicTools.GetTestDataPath import GetTestDataPath
from PublicTools.globalpy import GLOBAL_token

from PublicTools.globalpy import GLOBAL_TestDataPath

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_get_huoqunvshenkaliebiao():
    for i in range(3, 4):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-1-" + str(i + 1)
        htestcassname = "女神卡模块获取女神卡列表 V1" + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'card', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqunvshenkaxiangqing():
    for i in range(13, 17):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet

        if i == 16:
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
        htestcassid = "8-2-" + str(i + 1)
        htestcassname = "女神卡模块获取女神卡详情 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'card/detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_jiancenvshenkazhuangtai():
    for i in range(26, 29):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet

        hdata = {
            "id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-3-" + str(i + 1)
        htestcassname = "女神卡模块检测女神卡状态 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'card/check', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquyonghufeitiyannvshenkaid():
    for i in range(36, 38):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet

        if i == 37:
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
        htestcassid = "8-4-" + str(i + 1)
        htestcassname = "女神卡模块获取用户非体验女神卡idV1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'card/user-card', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_nvshenkaliebiaov1():
    for i in range(44, 46):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet

        hdata = {
            "filter": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-5-" + str(i + 1)
        htestcassname = "女神卡模块女神卡列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'card/card-list', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_nvshenkaliebiaov311():
    for i in range(54, 56):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet

        hdata = {
            "filter": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-6-" + str(i + 1)
        htestcassname = "女神卡模块女神卡列表 迭代3.1.1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'card/lteration-card-list', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_nvshenkaliebiaov312():
    for i in range(62, 63):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-7-" + str(i + 1)
        htestcassname = "女神卡模块女神卡列表 迭代3.1.2" + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'card/lteration-card', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_nvshenkalibiaozhimaxingyong():
    for i in range(72, 73):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-8-" + str(i + 1)
        htestcassname = "女神卡模块女神卡列表 芝麻信用调用" + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'card/z-card-list', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_zhimaxinyongkaliebiao():
    for i in range(85, 86):
        table = Testdata.sheets()[8]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "8-9-" + str(i + 1)
        htestcassname = "女神卡模块芝麻信用卡列表" + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'card/z-card-list', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
'''
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
'''
# test_get_peizhiwenjiangengxin()


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
