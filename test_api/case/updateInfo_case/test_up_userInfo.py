#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/120:11
# 文件     ：test_up_userInfo.py

from case.updateInfo_case.updateInfo import up_userInfo
import pytest
import allure

@allure.story('修改个人信息接口测试')
@allure.title('修改自己的个人信息，修改成功')
def test_up_userInfo_01(login):
    r = up_userInfo(login, age='18')
    assert r['message'] == 'update some data!'
    assert r['data']['name'] == 'test_hlp'

@allure.story('修改个人信息接口测试')
@allure.title('修改他人用户信息，修改失败提示无权限操作')
def test_up_userInfo_02(login):
    r = up_userInfo(login, name='test')
    assert r['message'] == '无权限操作'
    assert r['code'] == 4000

@allure.story('修改个人信息接口测试')
@allure.title('修改sex参数（F、M），修改成功')
@pytest.mark.parametrize('test_input', ['M', 'F'])
def test_up_userInfo_03(login, test_input):
    r = up_userInfo(login, sex=test_input)
    assert r['message'] == 'update some data!'
    assert r['code'] == 0

@allure.story('修改个人信息接口测试')
@allure.title('修改sex信息，传入错误的类型，修改失败')
def test_up_userInfo_04(login):
    r = up_userInfo(login, sex='X')
    assert r['message'] == '参数类型错误'
    assert r['code'] == 3333

if __name__ == '__main__':
    pytest.main('-s', 'test_up_userInfo.py')