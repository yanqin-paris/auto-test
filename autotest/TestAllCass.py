# -*- coding:utf-8 -*-

'''
Created on 2017年9月5日

@author: Jim

'''
# 导入测试用例
import time
import TestCass.TestCass_tongyong
import TestCass.TestCass_yonghu
import TestCass.TestCass_huodong
import TestCass.TestCass_dingdan
from PublicTools.log import logger


def TestCass_tongyong_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_tongyong.test_get_banbengengxin()
    TestCass.TestCass_tongyong.test_get_huodongzige()
    TestCass.TestCass_tongyong.test_get_jianchashoujihao()
    TestCass.TestCass_tongyong.test_get_peizhiwenjiangengxin()
    TestCass.TestCass_tongyong.test_get_pophuodong()
    logger.info("结束测试")


def TestCass_yonghu_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    # TestCass.TestCass_yonghu.test_post_duanxindenglu()
    # TestCass.TestCass_yonghu.test_post_mimadenglu()
    TestCass.TestCass_yonghu.test_get_huiyuanzhongxinshouyeshuju()
    TestCass.TestCass_yonghu.test_post_xiugaimima()
    TestCass.TestCass_yonghu.test_get_quanbuhuiyuantequan()
    TestCass.TestCass_yonghu.test_post_fenxiangmeiyijianglijifen()
    TestCass.TestCass_yonghu.test_get_wodenvshenkadingdan()
    TestCass.TestCass_yonghu.test_get_wodenvshenkadingdan2()
    TestCass.TestCass_yonghu.test_get_wodenvshenkadingdanxiangqing()
    TestCass.TestCass_yonghu.test_get_wodenvshenkadingdanxiangqing2()
    TestCass.TestCass_yonghu.test_get_wodeshouyeshuju()
    TestCass.TestCass_yonghu.test_get_wodeshouyeshuju2()
    TestCass.TestCass_yonghu.test_get_wodeshouyedingdanheyichushuju()
    TestCass.TestCass_yonghu.test_post_shoucangshangpin()
    TestCass.TestCass_yonghu.test_get_liulanjilu()
    TestCass.TestCass_yonghu.test_get_xiaoxizhongxin()
    TestCass.TestCass_yonghu.test_post_tianjiahuiyuanpeisongdizhi()
    TestCass.TestCass_yonghu.test_post_gengxinhuiyuanpeisongdizhi()
    TestCass.TestCass_yonghu.test_get_huoquyonghupingtuandingdanxinximzhan()
    TestCass.TestCass_yonghu.test_get_yonghuyajinrenzhengjinqian()
    TestCass.TestCass_yonghu.test_get_jifenmingxi()
    TestCass.TestCass_yonghu.test_get_qiandaoyemian()
    TestCass.TestCass_yonghu.test_get_huoquyouhuiquanliebiao()
    TestCass.TestCass_yonghu.test_get_huoquhuiyuanpeisongdizhi()
    TestCass.TestCass_yonghu.test_get_huoqulishiyouhuiquanliebiao()
    TestCass.TestCass_yonghu.test_get_huoqushiminrenzhengxinxi()
    TestCass.TestCass_yonghu.test_get_huoqukaipiaojiluliebiao()
    TestCass.TestCass_yonghu.test_get_huoquwodexinyuandanliebiao()
    TestCass.TestCass_yonghu.test_get_huoquwodeqianbao()
    TestCass.TestCass_yonghu.test_get_huoquyonghujibenxinxi()
    logger.info("结束测试")


def TestCass_huodong_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_huodong.test_get_huoqupingtuanhuodngxiangqing()
    logger.info("结束测试")


def TestCass_dingdan_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_dingdan.test_post_kaituanmzhan()
    TestCass.TestCass_dingdan.test_post_cantuanmzhan()
    TestCass.TestCass_dingdan.test_post_pingtuankadancigoumai()
    logger.info("结束测试")
