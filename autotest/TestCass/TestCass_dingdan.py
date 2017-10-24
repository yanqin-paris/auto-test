# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
import TestCass.TestCass_zulinjihua
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.TestRequest import TestDeleteRequest
from PublicTools.globalpy import GLOBAL_token
from PublicTools.globalpy import GLOBAL_TestDataPath
from PublicTools.globalpy import GLOBAL_testdb
from PublicTools.mydb import MyDB
from PublicTools.GetTestDataPath import GetDbConfigPath
import configparser
from PublicTools.GetTestDataPath import GetenvironmentPath
from PublicTools.time import shijiancuo

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
user_id = table.cell(10, 1).value
sku_id = table.cell(11, 1).value

order_id = table.cell(13, 1).value
order_split_id = table.cell(14, 1).value
order_split_item_id = table.cell(15, 1).value
db = GLOBAL_testdb
access_token = GLOBAL_token
config = configparser.ConfigParser()
config.read(GetenvironmentPath())
environment = config['environment']['environment']

query = 'DELETE from user_dots_detail where user_id=%s'
data = (user_id)
db.execute_delete(query, data)


query = 'DELETE from wms_stock_used where sku_id=%s'
data = (sku_id)
db.execute_delete(query, data)

query = 'DELETE from wms_stock_used where sku_id=%s'
data = ('21526')
db.execute_delete(query, data)


'''
query = "UPDATE `order`,order_split,order_split_item set `order`.status=4,order_split.`status`=5,order_split_item.`status`=2 where `order`.id=order_split.m_order_id and order_split.id=order_split_item.split_order_id and `order`.id = %s"
data = (order_id)
GLOBAL_testdb.execute_update(query, data)
'''

variables = {}


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

#********************************************************************8


def test_get_zuyiceshi():
    for i in range(49, 52):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 51:
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
        htestcassid = "3-6-" + str(i + 1)
        htestcassname = "订单模块租衣检测 V35" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'order/rent-check-v3', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuanjiannvshenkashengjidingdan():
    for i in range(57, 59):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 58:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "coupon_id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "coupon_id": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-7-" + str(i + 1)
        htestcassname = "订单模块创建女神卡升级订单 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/card-upgrade', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuanjiannvshenkaxufeidingdan():
    for i in range(67, 71):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 70:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "card_id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "card_id": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-8-" + str(i + 1)
        htestcassname = "订单模块创建女神卡续费订单 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/membership', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuanjiannvshenkagoumaidingdan():
    for i in range(75, 78):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 77:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "card_id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "card_id": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-9-" + str(i + 1)
        htestcassname = "订单模块创建女神卡购买订单 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/card', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuanjiannvshenkagoumaidingdanV310():
    for i in range(85, 88):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 87:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "card_id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "card_id": table.cell(i, 1).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-10-" + str(i + 1)
        htestcassname = "订单模块创建女神卡购买订单 V310" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'order/lteration-card', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_zhifuwancheng():
    for i in range(93, 96):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 95:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "id": table.cell(i, 1).value,
                "type": table.cell(i, 2).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "id": table.cell(i, 1).value,
                "type": table.cell(i, 2).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-11-" + str(i + 1)
        htestcassname = "订单模块支付完成 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'order/payment-done', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_yonghuhuiyuankashoucixiadanjiancha():
    for i in range(103, 105):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 104:
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
        htestcassid = "3-12-" + str(i + 1)
        htestcassname = "订单模块用户会员卡首次下单检查 V132" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/daily-first', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuangjianrichangzulindingdan():
    result = TestCass.TestCass_zulinjihua.test_post_tianjiayidaishangpin()
    if "error" in result:
        variables['plan_id'] = ""
        variables['plan_item_id'] = ""
    else:
        variables['plan_id'] = result['data']['plan_id']
        variables['plan_item_id'] = result['data']['items'][0]['plan_item_id']
    for i in range(111, 112):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "plan_id": variables['plan_id'],
            "user_address_id": table.cell(i, 2).value,
            "order_item": [{"plan_item_id": variables['plan_item_id']}],
            "remark": '配送前来电确认'
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-13-" + str(i + 1)
        htestcassname = "订单模块创建日常租赁订单积点付费 V3" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
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


def test_get_dingdanxiangqing():
    for i in range(399, 401):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet

        if i == 400:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "id": variables['order_id']
            }

        else:
            hdata = {
                "access_token": access_token,
                "id": variables['order_id']
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-42-" + str(i + 1)
        htestcassname = "用户模块订单详情 迭代310" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_dingdanxiangqing()


def test_delete_zulingoumaidingdanquxiao():
    for i in range(121, 122):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "order_id": variables['order_id'],
            "reason": table.cell(i, 2).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-14-" + str(i + 1)
        htestcassname = "订单模块租赁购买订单取消 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestDeleteRequest(hurl + 'order', hdata, headers,
                          htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_delete_zulingoumaidingdanquxiao()


def test_get_xufeitaocanyemian():
    for i in range(129, 131):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 130:
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
        htestcassid = "3-15-" + str(i + 1)
        htestcassname = "订单模块续费套餐页面 V34" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/renewal-package-v2', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_xufeiquerenyemian():
    for i in range(137, 139):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 138:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "card_id": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "card_id": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-16-" + str(i + 1)
        htestcassname = "订单模块续费确认页面 V34" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'order/renewal-confirm', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquhuiyuanpeisongdizhi():
    for i in range(145, 147):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 146:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "logistices_days": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "logistices_days": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-17-" + str(i + 1)
        htestcassname = "订单模块 获取会员配送地址V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'order/address', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquhuanyijiluliebiao():
    for i in range(153, 155):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 154:
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
        htestcassid = "3-18-" + str(i + 1)
        htestcassname = "订单模块获取还衣记录列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/return', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_shengjiquerenyemian():
    for i in range(161, 163):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 162:
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
        htestcassid = "3-19-" + str(i + 1)
        htestcassname = "订单确认模块升级确认确认页面 V330" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/upgrade-confirm', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_jidianquerenye():
    for i in range(169, 171):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 170:
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
        htestcassid = "3-20-" + str(i + 1)
        htestcassname = "订单确认模块积点确认页面 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/dots-package', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_xufeiquerenye():
    for i in range(177, 179):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        if i == 178:
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
        htestcassid = "3-21-" + str(i + 1)
        htestcassname = "订单确认模块续费确认页面 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'order/renewal-package', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_dingdanquerenshouhuo():
    query = "UPDATE `order`,order_split,order_split_item set `order`.status=4,order_split.`status`=5,order_split_item.`status`=2 where `order`.id=order_split.m_order_id and order_split.id=order_split_item.split_order_id and `order`.id = %s"
    data = (variables['order_id'])
    if environment == 'test':
        testdb = MyDB(GetDbConfigPath(), 'TESTDB')
    elif environment == 'auto':
        testdb = MyDB(GetDbConfigPath(), 'AUTODB')
    testdb.execute_update(query, data)
    for i in range(185, 187):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 186:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "order_id": variables['order_id'],
                "order_split_id": variables['ordersplitid']
            }

        else:
            hdata = {
                "access_token": access_token,
                "order_id": variables['order_id'],
                "order_split_id": variables['ordersplitid']
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-22-" + str(i + 1)
        htestcassname = "订单模块订单确认收货 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'order/sign', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuangjianrichangxuzudingdan():
    for i in range(193, 195):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 194:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "order_id": variables['order_id'],
                "order_split_item_id": variables['ordersplititemid'],
                "start_date": shijiancuo(35),
                "end_date": shijiancuo(38)
            }

        else:
            hdata = {
                "access_token": access_token,
                "order_id": variables['order_id'],
                "order_split_item_id": variables['ordersplititemid'],
                "start_date": shijiancuo(35),
                "end_date": shijiancuo(38)
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-23-" + str(i + 1)
        htestcassname = "订单模块创建日常续租订单积点 V35" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'order/plan-relet-v3', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuangjianhuanyidingdan():
    for i in range(201, 203):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 202:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "user_address_id": table.cell(i, 1).value,
                "express_company": table.cell(i, 2).value,
                "get_bag_starttime": shijiancuo(5),
                "get_bag_endtime": shijiancuo(5),
                "split_order_id": variables['ordersplitid']
            }

        else:
            hdata = {
                "access_token": access_token,
                "user_address_id": table.cell(i, 1).value,
                "express_company": table.cell(i, 2).value,
                "get_bag_starttime": shijiancuo(5),
                "get_bag_endtime": shijiancuo(5),
                "split_order_id": variables['ordersplitid']
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-24-" + str(i + 1)
        htestcassname = "订单模块创建还衣订单 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'order/return', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_jisuanliwuzulindingdanjiage():
    for i in range(217, 218):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "region_code": table.cell(i, 1).value,
            "order_item": [{"cart_item_id": variables['cart_item_id']}]
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-26-" + str(i + 1)
        htestcassname = "计算模块计算礼服租凭订单价格 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'price/dress', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_post_chuangjianlifuzulindingdan():
    TestCass.TestCass_zulinjihua.test_post_tianjiagouwuchelifu()
    r = TestCass.TestCass_zulinjihua.test_get_huoqulifugouwucheshangpinliebiao()
    if "error" in r:
        variables['cart_item_id'] = ''
    else:
        variables['cart_item_id'] = r['data'][0]['items'][0]['cart_item_id']
    test_post_jisuanliwuzulindingdanjiage()
    for i in range(209, 211):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet
        if i == 210:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "user_address_id": table.cell(i, 1).value,
                "order_item": [{"cart_item_id": variables['cart_item_id']}]
            }

        else:
            hdata = {
                "access_token": access_token,
                "user_address_id": table.cell(i, 1).value,
                "order_item": [{"cart_item_id": variables['cart_item_id']}]
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "3-25-" + str(i + 1)
        htestcassname = "订单模块创建礼服租赁订单 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        rr = TestPostRequest(hurl + 'order/dress', hdata, headers,
                             htestcassid, htestcassname, htesthope, fanhuitesthope)
        if "error" in rr:
            variables['order_id'] = ''
        else:
            variables['order_id'] = rr['data']['order_id']
