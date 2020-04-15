#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/118:25
# 文件     ：test_userInfo.py

import allure
import pytest
import requests
import os


@allure.story('查询个人信息接口测试')
@allure.title('传入正确的token值，可以查询到个人信息')
def test_userInfo_01(login):
    url = os.environ["host"] + '/api/v1/userinfo'
    re = login.get(url)
    assert re.json()['msg'] == 'sucess!'
    assert re.json()['code'] == 0

@allure.story('查询个人信息接口测试')
@allure.title('传错误的token值，无法获取个人信息')
def test_userInfo_02():
    url = os.environ["host"] + '/api/v1/userinfo'
    re = requests.get(url)
    assert re.status_code == 401
    assert re.json()['detail'] == 'Authentication credentials were not provided.'

if __name__ == '__main__':
    pytest.main('-s', 'test_userInfo.py')