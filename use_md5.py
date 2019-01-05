#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_md5.py
@Time    :   2019/01/02 12:18:02
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import hashlib,hmac,random
#md5加密
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

#hmac专业加密
def hmac_md5(key,s):
    return hmac.new(key.encode('utf-8'),s.encode('utf-8'),'MD5').hexdigest()

#定义用户类
class User(object):
    def __init__(self,username, password):
        self.username = username
        #随机的key值
        self.key =''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password =hmac_md5(self.key,password)
#储存用户数据
db = {}
#注册
def register(username,password):
    if username in db:
        print('该用户已注册')
    else:
        db[username] = User(username,password)
        print('注册成功')

#登录
def login(username,password):
    user = db[username]
    return user.password == hmac_md5(user.key,password)    
register('bob','12345')
register('bob','12345')
register('alice','12345')
assert login('alice', '12345')
# print(db)




# 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')