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

Testdata = xlrd.open_workbook(GetTestDataPath())  # 读取测试数据
table = Testdata.sheets()[0]  # 选择excle表中的sheet
hurl = table.cell(7, 1).value  # 从测试数据中读取url
htoken = table.cell(8, 1).value
hcontent_type = table.cell(6, 1).value
access_token = GLOBAL_token


def test_post_mimadenglu():
    for i in range(3, 6):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        hdata = {
            "mobile": table.cell(i, 0).value,
            "password": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-1-" + str(i + 1)
        htestcassname = "【用户模块】 密码登录 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/password-login', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)

# test_post_mimadenglu()


def test_post_duanxindenglu():
    for i in range(13, 16):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        hdata = {
            "mobile": table.cell(i, 0).value,
            "code": table.cell(i, 1).value
        }
        headers = {
            'content-type': hcontent_type,
            'token': htoken
        }
        htestcassid = "2-2-" + str(i + 1)
        htestcassname = "【用户模块】 会员登录 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/login', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_duanxindenglu()


def test_get_lingquyouhuiquan():
    for i in range(21, 26):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 25:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "type": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "type": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-3-" + str(i + 1)
        htestcassname = "【优惠券模块】 ​ 领取优惠券 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'coupon/receive', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_lingquyouhuiquan()


def test_get_huiyuanzhongxinshouyeshuju():
    for i in range(31, 34):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 32 or i == 33:
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
        htestcassid = "2-4-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 会员中心首页数据V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/member-centre', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huiyuanzhongxinshouyeshuju()


def test_post_xiugaimima():
    for i in range(39, 44):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 42:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "old_password": table.cell(i, 1).value,
                "password": table.cell(i, 2).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "old_password": table.cell(i, 1).value,
                "password": table.cell(i, 2).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-5-" + str(i + 1)
        htestcassname = "【用户模块】 修改密码 V1 " + htestcassid
        htesthope = table.cell(i, 3).value
        fanhuitesthope = table.cell(i, 4).value
        TestPostRequest(hurl + 'user/password', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_xiugaimima()


def test_get_quanbuhuiyuantequan():
    for i in range(49, 51):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 50:
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
        htestcassid = "2-6-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 全部会员特权V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/member-privilege', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_quanbuhuiyuantequan()


def test_post_fenxiangmeiyijianglijifen():
    for i in range(57, 60):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 58 or i == 59:
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
        htestcassid = "2-6-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 全部会员特权V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestPostRequest(hurl + 'user/share-success', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_fenxiangmeiyijianglijifen()


def test_get_wodenvshenkadingdan():
    for i in range(65, 68):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 66 or i == 67:
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
        htestcassid = "2-7-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单 V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/card-orders', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdan()


def test_get_wodenvshenkadingdan2():
    for i in range(71, 74):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 72 or i == 73:
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
        htestcassid = "2-8-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单 V1-3.2.0 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/lteration-card-orders', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdan2()


def test_get_wodenvshenkadingdanxiangqing():
    for i in range(77, 80):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 78:
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
        htestcassid = "2-9-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单详情 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/card-order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdanxiangqing()


def test_get_wodenvshenkadingdanxiangqing2():
    for i in range(83, 86):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 84:
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
        htestcassid = "2-10-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的女神卡订单详情 V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/lteration-card-order-detail', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodenvshenkadingdanxiangqing2()


def test_get_wodeshouyeshuju():
    for i in range(89, 91):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 90:
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
        htestcassid = "2-11-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的首页数据V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodeshouyeshuju()


def test_get_wodeshouyeshuju2():
    for i in range(95, 97):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 96:
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
        htestcassid = "2-12-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的首页数据V3.1.1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/lteration', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodeshouyeshuju2()


def test_get_wodeshouyedingdanheyichushuju():
    for i in range(105, 107):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 106:
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
        htestcassid = "2-13-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 我的首页订单和衣橱数据V3.1.1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/lteration-other', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_wodeshouyedingdanheyichushuju()


def test_post_shoucangshangpin():
    for i in range(115, 117):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 116:
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
        htestcassid = "2-14-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 收藏商品V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/wish', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_shoucangshangpin()


def test_get_liulanjilu():
    for i in range(121, 123):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 122:
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
        htestcassid = "2-15-" + str(i + 1)
        htestcassname = "【用户模块】浏览记录 V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/browsing-history', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_liulanjilu()


def test_get_xiaoxizhongxin():
    for i in range(132, 134):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 133:
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
        htestcassid = "2-16-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 消息中心V1 " + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'common/message-center', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_xiaoxizhongxin()


def test_post_tianjiahuiyuanpeisongdizhi():
    for i in range(138, 141):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 139:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "contact_name": table.cell(i, 1).value,
                "region_code": table.cell(i, 2).value,
                "contact_mobile": table.cell(i, 3).value,
                "region_name": table.cell(i, 4).value,
                "address_detail": table.cell(i, 5).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "contact_name": table.cell(i, 1).value,
                "region_code": table.cell(i, 2).value,
                "contact_mobile": table.cell(i, 3).value,
                "region_name": table.cell(i, 4).value,
                "address_detail": table.cell(i, 5).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-17-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 添加会员配送地址V1" + htestcassid
        htesthope = table.cell(i, 6).value
        fanhuitesthope = table.cell(i, 7).value
        TestPostRequest(hurl + 'user/address', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_tianjiahuiyuanpeisongdizhi()


def test_post_gengxinhuiyuanpeisongdizhi():
    for i in range(148, 151):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 149:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "id": table.cell(i, 1).value,
                "contact_name": table.cell(i, 2).value,
                "region_code": table.cell(i, 3).value,
                "contact_mobile": table.cell(i, 4).value,
                "region_name": table.cell(i, 5).value,
                "address_detail": table.cell(i, 6).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "id": table.cell(i, 1).value,
                "contact_name": table.cell(i, 2).value,
                "region_code": table.cell(i, 3).value,
                "contact_mobile": table.cell(i, 4).value,
                "region_name": table.cell(i, 5).value,
                "address_detail": table.cell(i, 6).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-18-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 更新会员配送地址V1" + htestcassid
        htesthope = table.cell(i, 7).value
        fanhuitesthope = table.cell(i, 8).value
        TestPostRequest(hurl + 'user/address', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_gengxinhuiyuanpeisongdizhi()


def test_get_huoquyonghupingtuandingdanxinximzhan():
    for i in range(159, 161):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 160:
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
        htestcassid = "2-19-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取用户的拼团订单信息 m站" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/team-buy-list', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquyonghupingtuandingdanxinximzhan()


def test_post_tianjiadingyuepingpai():
    for i in range(170, 173):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 172:
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
        htestcassid = "2-20-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 添加订阅品牌V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestPostRequest(hurl + 'user/brands', hdata, headers,
                        htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_post_tianjiadingyuepingpai()


def test_get_yonghuyajinrenzhengjinqian():
    for i in range(181, 183):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 182:
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
        htestcassid = "2-21-" + str(i + 1)
        htestcassname = "【用户模块】用户押金认证金钱 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/deposit-certificate', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_yonghuyajinrenzhengjinqian()


def test_get_jifenmingxi():
    for i in range(190, 192):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 191:
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
        htestcassid = "2-22-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 积分明细 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/points', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_jifenmingxi()


def test_get_qiandaoyemian():
    for i in range(201, 203):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 202:
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
        htestcassid = "2-23-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 签到页面V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/signs', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_qiandaoyemian()


def test_get_huoquyouhuiquanliebiao():
    for i in range(212, 214):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 213:
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
        htestcassid = "2-24-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取优惠券列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/coupon', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquyouhuiquanliebiao()


def test_get_huoquhuiyuanpeisongdizhi():
    for i in range(234, 236):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 235:
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
        htestcassid = "2-25-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取会员配送地址V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/address', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquhuiyuanpeisongdizhi()


def test_get_huoqulishiyouhuiquanliebiao():
    for i in range(245, 247):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 246:
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
        htestcassid = "2-26-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取历史优惠券列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/coupon-history', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqulishiyouhuiquanliebiao()


def test_get_huoqushiminrenzhengxinxi():
    for i in range(256, 258):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 257:
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
        htestcassid = "2-27-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取实名认证信息V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/realname', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqushiminrenzhengxinxi()


def test_get_huoqukaipiaojiluliebiao():
    for i in range(266, 268):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 267:
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
        htestcassid = "2-28-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取开票记录列表 V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/invoices', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoqukaipiaojiluliebiao()


def test_get_huoquwodexinyuandanliebiao():
    for i in range(277, 279):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 278:
            hdata = {
                "access_token": table.cell(i, 0).value,
                "type": table.cell(i, 1).value
            }

        else:
            hdata = {
                "access_token": access_token,
                "type": table.cell(i, 1).value
            }

        headers = {
            'content-type': hcontent_type
        }
        htestcassid = "2-29-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取我的心愿单列表V1 " + htestcassid
        htesthope = table.cell(i, 2).value
        fanhuitesthope = table.cell(i, 3).value
        TestGetRequest(hurl + 'user/wish', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquwodexinyuandanliebiao()


def test_get_huoquwodeqianbao():
    for i in range(286, 288):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 287:
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
        htestcassid = "2-30-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取我的钱包V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/wallet', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquwodeqianbao()


def test_get_huoquyonghujibenxinxi():
    for i in range(295, 297):
        table = Testdata.sheets()[2]  # 选择excle表中的sheet
        if i == 296:
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
        htestcassid = "2-31-" + str(i + 1)
        htestcassname = "【用户模块】 ​ 获取用户基本信息V1" + htestcassid
        htesthope = table.cell(i, 1).value
        fanhuitesthope = table.cell(i, 2).value
        TestGetRequest(hurl + 'user/show', hdata, headers,
                       htestcassid, htestcassname, htesthope, fanhuitesthope)
# test_get_huoquyonghujibenxinxi()
