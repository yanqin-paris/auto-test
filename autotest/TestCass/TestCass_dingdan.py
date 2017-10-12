# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim
'''
import xlrd
import TestCass.TestCass_zulinjihua
from PublicTools.TestRequest import TestGetRequestjiaqiang
from PublicTools.TestRequest import TestPostRequest
from PublicTools.TestRequest import TestGetRequest
from PublicTools.TestRequest import TestDeleteRequest
from PublicTools.GetTestDataPath import GetTestDataPath
from PublicTools.globalpy import GLOBAL_token

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token

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
        TestGetRequestjiaqiang(hurl + 'order/user-coupon', hdata, headers,
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
    TestCass.TestCass_zulinjihua.test_post_tianjiayidaishangpin()
    for i in range(111, 112):
        table = Testdata.sheets()[3]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "plan_id": TestCass.TestCass_zulinjihua.TestResults['plan_id'],
            "user_address_id": table.cell(i, 2).value,
            "order_item": [{"plan_item_id": TestCass.TestCass_zulinjihua.TestResults['plan_item_id']}],
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
    variables['order_id'] = r['data']['order_id']
# test_post_chuangjianrichangzulindingdan()


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
