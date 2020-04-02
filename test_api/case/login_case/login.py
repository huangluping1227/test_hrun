#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/116:38
# 文件     ：login.py

import requests
import os

def func_login(user, pwd):
    url = os.environ["host"] + '/api/v1/login'
    h = {'Content-Type': 'application/json'}
    body = {
        'username': user,
        'password': pwd
    }
    re = requests.post(url, json=body, headers=h)
    return re.json()
