#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/115:05
# 文件     ：test_regist.py

from case.regist_case.regist import register
import pytest
import allure


@allure.story('注册接口的测试用例')
@allure.title('输入未注册账号，注册成功')
def test_regist_01(delete_regist_data):
    '''
    :param delete_regist_data: 运行开始前，删除之前已经注册的数据
    :return:
    '''
    test_data = {"username": "test_hlp1111", "password": "123456", "mail": "123456@qq.com"}
    r1 = register(test_data)
    assert r1['code'] == 0
    assert r1['msg'] == '注册成功!'

@allure.story('注册接口的测试用例')
@allure.title('重复注册，注册失败')
def test_regist_02():
    '''
    :param delete_regist_data: 运行结束，删除刚注册的账户信息
    :return:
    '''
    test_data = {"username": "test_hlp", "password": "123456", "mail": "123456@qq.com"}
    r2 = register(test_data)
    assert r2['code'] == 2000
    assert r2['msg'] == 'test_hlp用户已被注册'
if __name__ == '__main__':
    pytest.main('-s', 'test_regist.py')