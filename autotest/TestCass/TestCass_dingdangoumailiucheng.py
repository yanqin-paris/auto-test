# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.globalpy import GLOBAL_token
from PublicTools.globalpy import GLOBAL_TestDataPath
from PublicTools.globalpy import GLOBAL_testdb
from PublicTools.mydb import MyDB
from PublicTools.GetTestDataPath import GetDbConfigPath
import configparser
from PublicTools.GetTestDataPath import GetenvironmentPath
from random import choice
Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
user_id = table.cell(10, 1).value
sku_id = table.cell(11, 1).value


db = GLOBAL_testdb
access_token = GLOBAL_token
config = configparser.ConfigParser()
config.read(GetenvironmentPath())
environment = config['environment']['environment']

query = 'DELETE FROM user_cart_plan where user_id=%s'
data = (user_id)
db.execute_delete(query, data)


query = 'DELETE FROM user_cart_plan_item where user_id=%s'
data = (user_id)
db.execute_delete(query, data)


variables = {}
specification_key = []
schedules = []
s = ()


def test_get_gengjuguanjianzisousuo():
    for i in range(3, 4):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet

        hdata = {
            "keyword": table.cell(i, 0).value,
            "mode": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-1-" + str(i + 1)
        htestcassname = "商品根据关键字搜索 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        r = TestGetRequest(hurl + 'product/keyword', hdata, headers,
                           htestcassid, htestcassname, htesthope, fanhuitesthope)
        variables['prdouct_id'] = r['data']['rows'][0]['id']


def test_get_huoqushangpinxiangqing():
    for i in range(13, 14):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet

        hdata = {
            "id": variables['prdouct_id']
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-2-" + str(i + 1)
        htestcassname = "商品获取商品详情 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        r = TestGetRequest(hurl + 'product', hdata, headers,
                           htestcassid, htestcassname, htesthope, fanhuitesthope)
        variables['specifications'] = r['data']['specifications'][0]['options']
        for specification in variables['specifications']:
            if specification['has_stock'] == 1:
                specification_key.append(specification['id'])
        variables['specification_key'] = choice(specification_key)


def test_get_huoqushangpinkejiezhouqi():
    for i in range(21, 22):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "region_code": table.cell(i, 1).value,
            "product_id": variables['prdouct_id'],
            "specification_key": variables['specification_key']
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-3-" + str(i + 1)
        htestcassname = "商品获取商品可借周期积点分离V33" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
        r = TestGetRequest(hurl + 'product-dots/schedule-v3', hdata, headers,
                           htestcassid, htestcassname, htesthope, fanhuitesthope)
        variables['schedules'] = r['data']['schedule']
        for schedule in variables['schedules']:
            s = (schedule['delivery_date'], schedule['default_return'])
            schedules.append(s)
        variables['schedule'] = choice(schedules)


def test_post_tianjiayidaishangpin():
    for i in range(31, 32):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "product_id": variables['prdouct_id'],
            "specification_key": variables['specification_key'],
            "delivery_region": table.cell(i, 3).value,
            "start_date": variables['schedule'][0],
            "end_date": variables['schedule'][1]
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-4-" + str(i + 1)
        htestcassname = "购物计划商品详情 添加衣袋商品积点 V36" + htestcassid
        htesthope = table.cell(i, 6).value
        fanhuitesthope = table.cell(i, 7).value
        r = TestPostRequest(hurl + 'plans-v3/product', hdata, headers,
                            htestcassid, htestcassname, htesthope, fanhuitesthope)
        if "error" in r:
            variables['plan_id'] = ""
            variables['plan_item_id'] = ""
        else:
            variables['plan_id'] = r['data']['plan_id']
            variables['plan_item_id'] = r['data']['items'][0]['plan_item_id']
    return r


def test_post_chuangjianrichangzulindingdan():
    for i in range(39, 40):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "plan_id": variables['plan_id'],
            "user_address_id": table.cell(i, 2).value,
            "order_item": [{"plan_item_id": variables['plan_item_id']}],
            "remark": table.cell(i, 4).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-5-" + str(i + 1)
        htestcassname = "订单模块创建日常租赁订单积点付费 V3" + htestcassid
        htesthope = table.cell(i, 5).value
        fanhuitesthope = table.cell(i, 6).value
        r = TestPostRequest(hurl + 'order/plan-daily-v3', hdata, headers,
                            htestcassid, htestcassname, htesthope, fanhuitesthope)
        if "error" in r:
            variables['order_id'] = ""
        else:
            variables['order_id'] = r['data']['order_id']
            query = "select `order`.id orderid,order_split.id ordersplitid,order_split_item.id  ordersplititemid from  `order`,order_split,order_split_item  where `order`.id=order_split.m_order_id and order_split.id=order_split_item.split_order_id and `order`.id = %s"
            data = (variables['order_id'])

            if environment == 'test':
                testdb = MyDB(GetDbConfigPath(), 'TESTDB')
            elif environment == 'auto':
                testdb = MyDB(GetDbConfigPath(), 'AUTODB')
            r = testdb.select_one_record(query, data)
            variables['ordersplitid'] = r['ordersplitid']
            variables['ordersplititemid'] = r['ordersplititemid']


def test_get_dingdanxiangqing_daifahuo():
    for i in range(57, 58):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "id": variables['order_id']
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-6-" + str(i + 1)
        htestcassname = "用户模块订单详情 迭代310" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def xiugaidingdanzhuangtai():
    query = "UPDATE `order`,order_split,order_split_item set `order`.status=4,order_split.`status`=5,order_split_item.`status`=2 where `order`.id=order_split.m_order_id and order_split.id=order_split_item.split_order_id and `order`.id = %s"
    data = (variables['order_id'])
    if environment == 'test':
        testdb = MyDB(GetDbConfigPath(), 'TESTDB')
    elif environment == 'auto':
        testdb = MyDB(GetDbConfigPath(), 'AUTODB')
    testdb.execute_update(query, data)


def test_get_dingdanxiangqing_yifahuo():
    for i in range(58, 59):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "id": variables['order_id']
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-7-" + str(i + 1)
        htestcassname = "用户模块订单详情 迭代310" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_dingdanquerenshouhuo():

    for i in range(49, 50):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "order_id": variables['order_id'],
            "order_split_id": variables['ordersplitid']
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-8-" + str(i + 1)
        htestcassname = "订单模块订单确认收货 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'order/sign', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_dingdanxiangqing_yishouhuo():
    for i in range(59, 60):
        table = Testdata.sheets()[10]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "id": variables['order_id']
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "10-9-" + str(i + 1)
        htestcassname = "用户模块订单详情 迭代310" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)