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
import TestCass.TestCass_shouye
import TestCass.TestCass_shangpin
import TestCass.TestCass_yuyue
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
    TestCass.TestCass_yonghu.test_get_yaoqingyoujiang()
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


def TestCass_shouye_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_shouye.test_get_huoquzhuantiguanlibiao()
    TestCass.TestCass_shouye.test_get_peizhiwenjiangengxin()
    TestCass.TestCass_shouye.test_get_huoqushouyeshuju()
    TestCass.TestCass_shouye.test_get_huoqupingpaixiangqing()
    TestCass.TestCass_shouye.test_get_huoqupingpaiguanshouye()
    logger.info("结束测试")


def TestCass_shangpin_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_shangpin.test_get_shangpinguanjianzilianxiang()
    TestCass.TestCass_shangpin.test_get_shangpingengxinessousuo()
    TestCass.TestCass_shangpin.test_get_gengjuguanjianzisousuo()
    TestCass.TestCass_shangpin.test_get_huoqutongpingpaishangpinlibiao()
    TestCass.TestCass_shangpin.test_get_huoqutongbiaoqianshangpinlibiao()
    TestCass.TestCass_shangpin.test_get_huoqushangpinshaixuanlibiao()
    TestCass.TestCass_shangpin.test_get_huoqushangpinpinglunlibiao()
    TestCass.TestCass_shangpin.test_get_huoqushangpinxiangqing()
    TestCass.TestCass_shangpin.test_get_huoqutuijianshangpinliebiao()
    TestCass.TestCass_shangpin.test_get_huoquxinpinshangpinlibiao()
    TestCass.TestCass_shangpin.test_get_huoqumashangchuanhuo24xiaoshishangpinliebiao()
    logger.info("结束测试")


def TestCass_yuyue_Cass():
    logger.info("开始测试")
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    logger.info(now)
    TestCass.TestCass_yuyue.test_get_huoquyuyueshijian()
    TestCass.TestCass_yuyue.test_delete_quxiaoyuyue()
    TestCass.TestCass_yuyue.test_post_chuanjianyuyueshenqing()
    TestCass.TestCass_yuyue.test_get_huoquyuyueliebiao()
    TestCass.TestCass_yuyue.test_get_yuyuexiangqing()
    logger.info("结束测试")
