#!/usr/bin/env python
# -*- coding:utf-8 -*-


from PublicTools.log import logger
from PublicTools.mydb import MyDB
from PublicTools.GetTestDataPath import GetTestConfigPath


logger.info('正在初始化数据库[名称：TESTDB]对象')
GLOBAL_testdb = MyDB(GetTestConfigPath() + 'dbconfig.conf', 'TESTDB')

'''
query = 'SELECT * FROM user_address WHERE id = %s or id = %s or id = %s'
data = ('1', '2', '3')

result = GLOBAL_testdb.select_many_record(query, data)
print(result[2]['address_detail'])
'''