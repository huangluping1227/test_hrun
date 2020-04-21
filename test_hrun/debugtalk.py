#_*_coding:utf-8_*_
# 作者:       Administrator
# 创建时间:   2020/4/20 19:40
# 文件:       debugtalk.py
# IDE:        PyCharm

from common.connectMysql import dbConnect
import requests
import os

def select(sql):
    '''对数据库进行查询'''
    db = dbConnect()
    re = db.select(sql)
    return re

def execute(sql):
    '''对数据库进行增删改的操作'''
    db = dbConnect()
    r = db.operation(sql)
    return r

def login(user, psw):
    '''登录返回token'''
    url = 'http://49.235.92.12:9000/api/v1/login'
    data = {
        'username': user,
        'password': psw
    }
    re = requests.post(url, json=data)
    return re.json()['token']

# def setup_login(user, psw, request):
#     token = login(user, psw)
#     request['headers'] = 'Authorization: Token %s' % token
#     print(request)

def ENV(keyname):
    '''
    获取环境keyname对应的值
    :param keyname:
    :return: 返回环境值
    '''
    value = os.environ.get(keyname)
    return value