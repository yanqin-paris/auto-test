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
from PublicTools.globalpy import GLOBAL_testdb

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token

query = 'delete from user_base_information where user_id=%s'
data = ('15903',)
GLOBAL_testdb.execute_delete(query, data)


def test_get_huoqupingtuanhuodngxiangqing():
    for i in range(3, 5):
        table = Testdata.sheets()[4]  # 选择excle表中的sheet
        if i == 4:
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
        htestcassid = "4-1-" + str(i + 1)
        htestcassname = "活动模块获取拼团活动详情 m站" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'activity/team-buying', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqupingtuanhuodngxiangqing()


def test_get_huoqudiaochawenjuanjibenxinxi():
    for i in range(13, 14):
        table = Testdata.sheets()[4]  # 选择excle表中的sheet

        hdata = {
            "access_token": access_token

        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "4-2-" + str(i + 1)
        htestcassname = "活动模块获取调查问卷基本信息" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'activity/questionnaire', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqudiaochawenjuanjibenxinxi()


def test_post_diaochawenjuanjibenxinxitijiao():
    for i in range(21, 23):
        table = Testdata.sheets()[4]  # 选择excle表中的sheet
        hdata = {
            "access_token": access_token,
            "dob": table.cell(i, 1).value,
            "fit_height": table.cell(i, 2).value,
            "fit_weight": table.cell(i, 3).value,
            "size": table.cell(i, 4).value,
            "bust": table.cell(i, 5).value,
            "waistline": table.cell(i, 6).value,
            "hips": table.cell(i, 7).value,
            "body_type": table.cell(i, 8).value,
            "clothing_style": table.cell(i, 9).value,
            "job": table.cell(i, 10).value,
            "clothing_monthly_consumption": table.cell(i, 11).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "4-3-" + str(i + 1)
        htestcassname = "活动模块调查问卷基本信息提交 " + htestcassid
        htesthope = table.cell(i, 12).value
        fanhuitesthope = table.cell(i, 13).value
        TestPostRequest(hurl + 'activity/questionnaire', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_diaochawenjuanjibenxinxitijiao()
