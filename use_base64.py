#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_base64.py
@Time    :   2019/01/02 10:55:19
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import base64

def safe_base64_decode(s):
    num = len(s)%4
    if num!=0:
        for i in range(num):
            s+=b'='
    return base64.b64decode(s)

# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
