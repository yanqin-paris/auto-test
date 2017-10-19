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

from PublicTools.globalpy import GLOBAL_TestDataPath

Testdata = xlrd.open_workbook(GLOBAL_TestDataPath)  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_get_banbengengxin():
    for i in range(3, 6):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = {
            "platform": table.cell(i, 0).value,
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-1-" + str(i + 1)
        htestcassname = "通用版本更新检查 V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'common/version', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_banbengengxin()


def test_get_huodongzige():
    for i in range(13, 15):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        if i == 13:
            hdata = {
                "access_token": access_token,
                "code": table.cell(i, 1).value
            }
        else:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "code": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-2-" + str(i + 1)
        htestcassname = "通用用户活动资格检查 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'common/check-activity', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_huodongzige()


def test_get_jianchashoujihao():
    for i in range(21, 24):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = {
            "mobile": table.cell(i, 0).value,
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-3-" + str(i + 1)
        htestcassname = "通用模块 检查手机号 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'common/mobile', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_jianchashoujihao()


def test_get_peizhiwenjiangengxin():
    for i in range(31, 32):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-4-" + str(i + 1)
        htestcassname = "通用配置文件更新 V1 " + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'common/configs', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_peizhiwenjiangengxin()


def test_get_pophuodong():
    for i in range(40, 41):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = ''
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-5-" + str(i + 1)
        htestcassname = "通用模块POP活动V1 " + htestcassid
        htesthope = table.cell(i, 0).value
        fanhuitesthope = table.cell(i, 1).value
        TestGetRequest(hurl + 'common/advertising', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_pophuodong()


def test_get_huoquwuliutianshu():
    for i in range(48, 51):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = {
            "region_code": table.cell(i, 0).value,
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-6-" + str(i + 1)
        htestcassname = "通用模块获取物流天数 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'common/express-days', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)


def test_get_huoquwuliutianshudiedai():
    for i in range(57, 60):
        table = Testdata.sheets()[1]  # 选择excle表中的sheet
        hdata = {
            "region_code": table.cell(i, 0).value,
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "1-7-" + str(i + 1)
        htestcassname = "通用模块获取物流天数迭代版本" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'common/express-days-v2', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
