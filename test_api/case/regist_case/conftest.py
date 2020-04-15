#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/116:14
# 文件     ：conftest.py
from common.connect_mysql import ConnectMysql
import pytest

@pytest.fixture()
def delete_regist_data():
    db = ConnectMysql(host='49.235.92.12', db='apps', port=3309)

    select_sql = "SELECT * FROM auth_user WHERE username = 'test_hlp1111';"
    delete_sql = "DELETE FROM auth_user WHERE username = 'test_hlp1111';"


    # 前置操作：先查询数据库是否存在test_hlp用户，存在则要删除
    if db.select(select_sql):
        db.operation(delete_sql)
    yield
    print('后置条件，删除刚注册的账户')
    result = db.operation(delete_sql)
    db.close()
    print(result)