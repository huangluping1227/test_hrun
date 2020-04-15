#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/119:04
# 文件     ：conftest.py

import pytest
import requests
from common.connect_mysql import ConnectMysql

host = 'http://49.235.92.12:9000'
@pytest.fixture(scope='module')
def creat_data():
    db = ConnectMysql(host='49.235.92.12', db='apps', port=3309)
    select_sql = "SELECT * FROM auth_user WHERE username = 'test_hlp';"
    insert_sql = '''INSERT INTO auth_user(`password`, `username`, `email`, `is_staff`, `is_active`, `date_joined`)
        VALUES('pbkdf2_sha256$100000$2F3XChjcqHxN$ddJgxZU0zozEPoJ2ykbfjCT4E9KqG/jSoj52xE9bsdQ=', 'test_hlp',
        '2990444561@qq.com', 0, 1, '2020-01-30 03:00:59.661919');'''
    # 判断test_hlp是否存在，不存在则需要添加
    if not db.select(select_sql):
        db.operation(insert_sql)
        db.close()

# 登录之前先查询用户是否存在
@pytest.fixture(scope='module')
def login(creat_data):
    s = requests.session()
    url = host + '/api/v1/login'
    body = {
        'username': 'test_hlp',
        'password': '123456'
    }
    r = s.post(url, json=body)
    token = r.json()['token']
    # 更新token
    header = {'Authorization': 'Token %s' % token}
    s.headers.update(header)
    return s
