#!/usr/bin/env python
# -*- coding:utf-8 -*-

import configparser
import sys
import pymysql.cursors

from PublicTools.log import logger


class MyDB:
    """动作类，获取数据库连接，配置数据库IP，端口等信息，获取数据库连接"""

    def __init__(self, config_file, db):
        config = configparser.ConfigParser()

        # 从配置文件中读取数据库服务器IP、域名，端口
        config.read(config_file)
        host = config[db]['host']
        port = config[db]['port']
        user = config[db]['user']
        passwd = config[db]['passwd']
        db_name = config[db]['db']
        charset = config[db]['charset']

        try:
            self.dbconn = pymysql.connect(host=host,
                                          user=user,
                                          password=passwd,
                                          db=db_name,
                                          charset=charset,
                                          cursorclass=pymysql.cursors.DictCursor
                                          )

        except pymysql.err.OperationalError as e:
            logger.error('初始化数据连接失败：%s' % e)
            sys.exit()

    def get_conn(self):
        return self.dbconn

    def execute_create(self, query):
        logger.info('query：%s' % query)
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            logger.error('创建数据库表操作失败：%s' % e)
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def execute_insert(self, query, data):
        logger.info('query：%s  data：%s' % (query, data))
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query, data)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            logger.error('执行数据库插入操作失败：%s' % e)
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def execute_delete(self, query, data):
        logger.info('query：%s  data：%s' % (query, data))
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query, data)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            logger.error('执行数据库删除操作失败：%s' % e)
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def execute_update(self, query):
        logger.info('query：%s' % query)
        try:
            db_cursor = self.dbconn.cursor()
            db_cursor.execute(query)
            db_cursor.execute('commit')
            return True
        except Exception as e:
            logger.error('执行数据库更新操作失败：%s' % e)
            db_cursor.execute('rollback')
            db_cursor.close()
            exit()

    def select_one_record(self, query, data=""):
        '''返回结果只包含一条记录'''
        logger.info('query：%s  data：%s' % (query, data))
        try:
            db_cursor = self.dbconn.cursor()
            if data:
                db_cursor.execute(query, data)
            else:
                db_cursor.execute(query)
            query_result = db_cursor.fetchone()
            return query_result
        except Exception as e:
            logger.error('执行数据库查询操作失败：%s' % e)
            db_cursor.close()
            exit()

    def select_many_record(self, query, data=""):
        '''返回结果只包含多条记录'''
        logger.info('query：%s  data：%s' % (query, data))
        try:
            db_cursor = self.dbconn.cursor()
            if data:
                db_cursor.execute(query, data)
            else:
                db_cursor.execute(query)
            query_result = db_cursor.fetchall()
            return query_result
        except Exception as e:
            logger.error('执行数据库查询操作失败：%s' % e)
            db_cursor.close()
            exit()

    def close(self):
        self.dbconn.close

if __name__ == '__main__':
    query = 'SELECT * FROM user_address WHERE id = %s'
    data = ('1',)
    testdb = MyDB('D:\\autotestapi\\autotest\\config\\dbconfig.conf', 'TESTDB')
    result = testdb.select_one_record(query, data)
    print(result)

'''
        query = 'SELECT count(testcase_id) FROM ' + testcase_report_tb + ' WHERE executed_history_id = %s'
        data = (executed_history_id,)
        result = testdb.select_one_record(query, data)
        self.case_total = result[0]
        query = ('SELECT testcase_id, testcase_name, project, testplan FROM ' + testcase_report_tb + \
                     ' WHERE project=%s AND testplan=%s AND executed_history_id = %s '\
                     ' GROUP BY testcase_id ORDER BY id ASC')
        data = (project, testplan, executed_history_id)
        result = testdb.select_many_record(query, data)
   '''
