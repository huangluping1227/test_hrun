#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/116:15
# 文件     ：connect_mysql.py

import pymysql

class ConnectMysql():
    def __init__(self, host='localhost', user='root', password='123456', db='test', port=3306):
        '''
        建立数据库连接
        :param host: host地址
        :param user: 连接数据库用户名
        :param password: 用户密码
        :param db: 数据库名
        :param port: mysql端口
        '''
        self.db = pymysql.connect(
            host=host,
            user=user,
            password=password,
            db=db,
            port=port
        )
        # 使用cursor()方法获取操作游标
        self.cursor = self.db.cursor()
    def select(self, sql):
        '''
        查询数据库
        :param sql: 查询sql语句
        :return: 查询结果
        '''
        self.cursor.execute(sql)
        results = self.cursor.fetchall() # fetchall()返回所有的查询结果
        return results
    def operation(self, sql):
        '''
        对数据库进行删除、新增、修改操作
        :param sql: 需要执行的sql语句
        :return:
        '''
        # try:
        if self.cursor.execute(sql) >= 1:
            self.db.commit()
            return '操作成功'
        # except:
        #     # 发生错误时回滚
        #     self.db.rollback()
    def close(self):
        # 关闭连接
        self.db.close()
if __name__ == '__main__':
    db = ConnectMysql(host='49.235.92.12', db='apps', port=3309)
    sql = '''SELECT * FROM auth_user WHERE username = 'test_hlp';'''
    db.select(sql)
    db.close()

