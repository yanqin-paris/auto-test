# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.TestRequest import TestDeleteRequest
from PublicTools.globalpy import GLOBAL_token
from PublicTools.time import shijiancuo

from PublicTools.globalpy import GLOBAL_TestDataPath

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token

TestResults = {}


def test_post_tianjiayidaishangpin():
    for i in range(21, 23):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
        print(table.cell(i, 1).value)
        hdata = {
            "access_token": access_token,
            "product_id": table.cell(i, 1).value,
            "specification_key": table.cell(i, 2).value,
            "delivery_region": table.cell(i, 4).value,
            "start_date": shijiancuo(30),
            "end_date": shijiancuo(34)
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-1-" + str(i + 1)
        htestcassname = "购物计划商品详情 添加衣袋商品积点 V36" + htestcassid
        htesthope = table.cell(i, 7).value
        fanhuitesthope = table.cell(i, 8).value
        r = TestPostRequest(hurl + 'plans-v3/product', hdata, headers,
                            htestcassid, htestcassname, htesthope, fanhuitesthope)
        if "error" in r:
            TestResults['plan_id'] = ""
            TestResults['plan_item_id'] = ""
        else:
            TestResults['plan_id'] = r['data']['plan_id']
            TestResults['plan_item_id'] = r['data']['items'][0]['plan_item_id']
    return r


def test_post_jisuanrichangzulindingdanjiage():
    for i in range(67, 68):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "plan_id": TestResults['plan_id'],
            "region_code": table.cell(i, 2).value,
            "order_item": [{"plan_item_id": TestResults['plan_item_id']}]
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-8-" + str(i + 1)
        htestcassname = "计算模块计算日常租赁订单价格积点 V3" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
        TestPostRequest(hurl + 'price/plan-daily-v3', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_post_jisuanrichangzulindingdanjiage()


def test_get_huoquyidaishangpinxiangqinghuoqu():
    for i in range(57, 58):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "plan_id": TestResults['plan_id'],
            "product_id": table.cell(i, 2).value,
            "specification_key": table.cell(i, 3).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-6-" + str(i + 1)
        htestcassname = "租赁计划商品详情 获取衣袋商品详情获取 积点 V36" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
        TestGetRequest(hurl + 'plans-v3/items', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqugouwujihuahegouwucheyitianjiashangpinshuliang():
    for i in range(13, 15):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
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
        htestcassid = "11-7-" + str(i + 1)
        htestcassname = "购物计划获取购物计划和购物车内已添加商品数量 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'plans/amount', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquyouxiaoyidai():
    for i in range(49, 50):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "product_id": table.cell(i, 1).value,
            "specification_key": table.cell(i, 2).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-5-" + str(i + 1)
        htestcassname = "租赁计划商品详情 获取有效的衣袋 V36" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
        TestGetRequest(hurl + 'plans-v3/valid-plan', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_xianshisuoyouqiehuanyidai():
    for i in range(39, 40):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "product_id": table.cell(i, 1).value,
            "specification_key": table.cell(i, 2).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-4-" + str(i + 1)
        htestcassname = "租赁计划商品详情 显示所有切换衣袋 V36" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestGetRequest(hurl + 'plans-v3/all-plan', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquyitianjiayidai():
    for i in range(3, 5):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet

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
        htestcassid = "11-3-" + str(i + 1)
        htestcassname = "租赁计划商品列表 获取已添加的衣袋 v36" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'plans-v3/filter', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_delete_shanchuyidaishangpin():
    for i in range(31, 32):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "plan_id": TestResults['plan_id'],
            "plan_item_id": TestResults['plan_item_id'],
            "product_id": table.cell(i, 3).value,
            "specification_key":  table.cell(i, 4).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-2-" + str(i + 1)
        htestcassname = "租赁计划商品详情 删除衣袋商品 V36" + htestcassid
        htesthope = table.cell(i, 5).value
        fanhuitesthope = table.cell(i, 6).value
        TestDeleteRequest(hurl + 'plans-v3/product', hdata, headers,
                          htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_tianjiagouwuchelifu():
    for i in range(75, 76):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "product_id": table.cell(i, 1).value,
            "specification_key": table.cell(i, 2).value,
            "delivery_region": table.cell(i, 3).value,
            "delivery_region_name": table.cell(i, 4).value,
            "start_date": shijiancuo(10),
            "end_date": shijiancuo(12)
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "11-9-" + str(i + 1)
        htestcassname = "购物车添加购物车礼服 V1" + htestcassid
        htesthope = table.cell(i, 5).value
        fanhuitesthope = table.cell(i, 6).value
        TestPostRequest(hurl + 'cart/product', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqulifugouwucheshangpinliebiao():
    for i in range(85, 86):
        table = Testdata.sheets()[11]  # 选择excle表中的sheet

        if i == 86:
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
        htestcassid = "11-10-" + str(i + 1)
        htestcassname = "购物袋获取礼服购物车商品列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        r = TestGetRequest(hurl + 'cart/dress', hdata, headers,
                           htestcassid, htestcassname, htesthope, fanhuitesthope)
    return r
