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


def test_get_shangpinguanjianzilianxiang():
    for i in range(3, 4):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "keyword": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-1-" + str(i + 1)
        htestcassname = "商品关键字联想" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'product/autocomplete', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_shangpinguanjianzilianxiang()


def test_get_shangpingengxinessousuo():
    for i in range(13, 16):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-2-" + str(i + 1)
        htestcassname = "商品更新ES搜索" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'product/esupdate', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_shangpingengxinessousuo()


def test_get_gengjuguanjianzisousuo():
    for i in range(21, 24):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "keyword": table.cell(i, 0).value,
            "mode": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-3-" + str(i + 1)
        htestcassname = "商品根据关键字搜索 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'product/keyword', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_get_gengjuguanjianzisousuo()


def test_get_huoqutongpingpaishangpinlibiao():
    for i in range(31, 36):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "brand_id": table.cell(i, 0).value,
            "mode": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-4-" + str(i + 1)
        htestcassname = "商品获取同品牌商品列表 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'product/brand', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqutongpingpaishangpinlibiao()


def test_get_huoqutongbiaoqianshangpinlibiao():
    for i in range(44, 47):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "tag_id": table.cell(i, 0).value,
            "category_id": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-5-" + str(i + 1)
        htestcassname = "商品获取同标签商品列表 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'product/tags', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqutongbiaoqianshangpinlibiao()


def test_get_huoqushangpinshaixuanlibiao():
    for i in range(54, 58):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "mode": table.cell(i, 0).value,
            "type": table.cell(i, 1).value,
            "use_limit_days": table.cell(i, 2).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-6-" + str(i + 1)
        htestcassname = "商品获取商品筛选列表 V1" + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestGetRequest(hurl + 'product/filter', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqushangpinshaixuanlibiao()


def test_get_huoqushangpinpinglunlibiao():
    for i in range(67, 69):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "product_id": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-7-" + str(i + 1)
        htestcassname = "商品获取商品评论列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'product/comments', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqushangpinpinglunlibiao()


def test_get_huoqushangpinxiangqing():
    for i in range(77, 79):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "id": table.cell(i, 0).value,
            "only_specifications": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-8-" + str(i + 1)
        htestcassname = "商品获取商品详情 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'product', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqushangpinxiangqing()


def test_get_huoqutuijianshangpinliebiao():
    for i in range(85, 88):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "type": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-9-" + str(i + 1)
        htestcassname = "商品获取推荐商品列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'product/recommend', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqutuijianshangpinliebiao()


def test_get_huoquxinpinshangpinlibiao():
    for i in range(95, 98):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "type": table.cell(i, 0).value,
            "filter": table.cell(i, 1).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-10-" + str(i + 1)
        htestcassname = "商品获取新品商品列表 V1" + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'product/newarrival', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquxinpinshangpinlibiao()


def test_get_huoqumashangchuanhuo24xiaoshishangpinliebiao():
    for i in range(108, 110):
        table = Testdata.sheets()[6]  # 选择excle表中的sheet
        hdata = {
            "filter": table.cell(i, 0).value
        }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "6-11-" + str(i + 1)
        htestcassname = "商品获取马上穿或24小时发货商品列表 V3.3" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'product/wear-right-away', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqumashangchuanhuo24xiaoshishangpinliebiao()
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
