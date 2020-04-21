#_*_coding:utf-8_*_
# 作者:       Administrator
# 创建时间:   2020/4/20 20:31
# 文件:       connectMysql.py
# IDE:        PyCharm

import pymysql

db_info = {
    "host": "49.235.92.12",
    "user": "root",
    "password": "123456",
    "database": "apps",
    "port": 3309
}

class dbConnect(object):
    '''
    连接mysql数据库并操作
    '''''
    def __init__(self):
        '''
        连接数据库
        '''
        self.db = pymysql.connect(**db_info)
        self.cursor = self.db.cursor()
    def select(self, sql):
        '''
        查询操作
        :param sql: 查询语句
        :return: 查询结果
        '''
        try:
            self.cursor.execute(sql)
            results = self.cursor.fetchall()
            return results
        finally:
            self.db.close()

    def operation(self, sql):
        '''
        对数据库进行删除、新增、修改操作
        :param sql: 需要执行的sql语句
        :return:
        '''
        try:
            if self.cursor.execute(sql) >= 1:
                self.db.commit()
                return '操作成功'
        except:
            # 发生错误时回滚
            self.db.rollback()
        finally:
            self.db.close()