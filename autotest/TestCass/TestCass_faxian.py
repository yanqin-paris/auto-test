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
from PublicTools.globalpy import GLOBAL_TestDataPath

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_post_guanzhuhuiyuan():
    for i in range(3, 5):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "id": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-1-" + str(i + 1)
        htestcassname = "发现模块关注会员 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'find/follow', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_delete_quxiaoguanzhuhuiyuan():
    for i in range(13, 15):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "id": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-2-" + str(i + 1)
        htestcassname = "发现模块 取消关注会员 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestDeleteRequest(hurl + 'find/follow', hdata, headers,
                          htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquhuiyuanzulinhuogoumaiguodeyifu():
    for i in range(21, 23):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        if i == 22:
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
        htestcassid = "9-3-" + str(i + 1)
        htestcassname = "发现模块获取会员租赁或购买过的衣服 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'find/clothes', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqufaxianliebiao():
    for i in range(31, 33):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "type": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-4-" + str(i + 1)
        htestcassname = "发现模块获取发现列表 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'find', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqushaidanyonghuxiangqing():
    for i in range(41, 42):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token,
            "id": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-5-" + str(i + 1)
        htestcassname = "发现模块获取晒单用户详情 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'find/user', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqushaituxiangqing():
    for i in range(51, 53):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-6-" + str(i + 1)
        htestcassname = "发现模块获取晒图详情V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'find/detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoqupinglunliebiao():
    for i in range(59, 60):
        table = Testdata.sheets()[9]  # 选择excle表中的sheet

        hdata = {
            "id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "9-7-" + str(i + 1)
        htestcassname = "发现模块获取评论列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'find/comments', hdata, headers,
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
