#_*_coding:utf-8_*_
# 作者     ：Administrator
# 创建时间 ：2020/4/114:52
# 文件     ：regist_case.py

# 注册
import requests
import os

def register(body):
    url = os.environ["host"] + '/api/v1/register'
    h = {'Content-Type': 'application/json'}
    re = requests.post(url, json=body, headers=h)
    return re.json()