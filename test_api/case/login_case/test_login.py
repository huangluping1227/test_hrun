#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/116:41
# 文件     ：test_login.py

from case.login_case.login import func_login
import allure
import pytest

@allure.story('测试登录接口')
@allure.title('输入正确的账号密码，登录成功')
def test_login_01(creat_data):
    user = 'test_hlp'
    pwd = '123456'
    r = func_login(user, pwd)
    assert r['code'] == 0
    assert r['msg'] == 'login success!'
    assert r['username'] == 'test_hlp'

@allure.story('测试登录接口')
@allure.title('输入未注册账号，登录失败')
def test_login_02():
    user = 'abcdef'
    pwd = '123456'
    r = func_login(user, pwd)
    assert r['code'] == 3003
    assert r['msg'] ==  "账号或密码不正确"

test_data = [('123456','123456'),('test_hlp','66666')]
@allure.story('测试登录接口')
@allure.title(' 输入错误的账号或密码，登录失败')
@pytest.mark.parametrize('user, pwd',test_data)
def test_login_03(user, pwd):
    r = func_login(user, pwd)
    assert r['code'] == 3003
    assert r['msg'] == "账号或密码不正确"

@allure.story('测试登录接口')
@allure.title(' 用户名或密码为空，登录失败')
@pytest.mark.parametrize('user, pwd',[('', '123456'),('test_hlp', '')])
def test_login_04(user, pwd):
    r = func_login(user, pwd)
    assert r['code'] == 3003
    assert r['msg'] == "账号或密码不正确"
if __name__ == '__main__':
    pytest.main('-s', 'test_login.py')