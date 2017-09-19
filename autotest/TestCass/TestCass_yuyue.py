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

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_get_huoquyuyueshijian():
    for i in range(3, 8):
        table = Testdata.sheets()[7]  # 选择excle表中的sheet
        if i == 7:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "date": table.cell(i, 1).value,
                "type": table.cell(i, 2).value,
                "store_id": table.cell(i, 3).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "date": table.cell(i, 1).value,
                "type": table.cell(i, 2).value,
                "store_id": table.cell(i, 3).value
            }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "7-1-" + str(i + 1)
        htestcassname = "预约模块获取预约时间V1" + htestcassid
        htesthope = table.cell(i, 4).value
        fanhuitesthope = table.cell(i, 5).value
        TestGetRequest(hurl + 'booking/time', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_huoquyuyueshijian()


def test_get_huoquyuyueliebiao():
    for i in range(21, 22):
        table = Testdata.sheets()[7]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "7-2-" + str(i + 1)
        htestcassname = "预约模块获取预约列表V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'booking', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquyuyueliebiao()


def test_get_yuyuexiangqing():
    for i in range(31, 32):
        table = Testdata.sheets()[7]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "7-3-" + str(i + 1)
        htestcassname = "预约模块预约详情V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'booking/info', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_yuyuexiangqing()


def test_delete_quxiaoyuyue():
    for i in range(39, 40):
        table = Testdata.sheets()[7]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "7-4-" + str(i + 1)
        htestcassname = "预约模块取消预约V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestDeleteRequest(hurl + 'booking/info', hdata, headers,
                          htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_delete_quxiaoyuyue()
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


def test_post_chuanjianyuyueshenqing():
    for i in range(13, 15):
        table = Testdata.sheets()[7]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "name": table.cell(i, 1).value,
            "mobile": table.cell(i, 2).value,
            "gender": table.cell(i, 3).value,
            "city_code": table.cell(i, 4).value,
            "store": table.cell(i, 5).value,
            "city_name": table.cell(i, 6).value,
            "type": table.cell(i, 7).value,
            "date": table.cell(i, 8).value,
            "start_time": table.cell(i, 9).value,
            "num": table.cell(i, 10).value,
            "channel": table.cell(i, 11).value,
            "remark": table.cell(i, 12).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "7-5-" + str(i + 1)
        htestcassname = "预约模块创建预约申请V1" + htestcassid
        htesthope = table.cell(i, 13).value
        fanhuitesthope = table.cell(i, 14).value
        TestPostRequest(hurl + 'booking/info', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_chuanjianyuyueshenqing()
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
