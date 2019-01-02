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
import hashlib
# db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
#设置
db = {}

# def login(user, password):
#     md5 = hashlib.md5()
#     md5.update(password.encode('utf-8'))
#     if db[user] == md5.hexdigest():
#         return True
#     return False



#md5加密
def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()

#定义用户类
class User(object):
    #所有实例共享
    db={}
    #注册
    def __init__(self,username, password):
        User.db[username] = get_md5(password+'xiqukeke')
    #登录
    def login(self,username,password):
        return User.db[username] == get_md5(password+'xiqukeke')

alice =User('alice','123456')
bob =User('bob','123456')
print(alice.login('bob','123456'))
# print(User.db)




# 测试:
# assert login('michael', '123456')
# assert login('bob', 'abc999')
# assert login('alice', 'alice2008')
# assert not login('michael', '1234567')
# assert not login('bob', '123456')
# assert not login('alice', 'Alice2008')
# print('ok')