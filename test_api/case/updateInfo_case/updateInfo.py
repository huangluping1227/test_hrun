#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/119:50
# 文件     ：updateInfo.py

import os

def up_userInfo(s, name='test_hlp', sex='M', age='20', mail='123456@qq.com'):
    url = os.environ["host"] + '/api/v1/userinfo'
    body = {
        "name": name,
        "sex": sex,
        "age": age,
        "mail": mail
    }
    r = s.post(url, json=body)
    return r.json()