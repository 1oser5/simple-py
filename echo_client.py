#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   echo_client.py
@Time    :   2019/01/04 16:01:23
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#建立连接
s.connect(('127.0.0.1',9999))
#接受欢迎消息
print(s.recv(1024).decode('utf-8'))
for data in [b'Alice',b'Trace',b'Bob']:
    #发送数据:
    s.send(data)
    print(s.recv(1024).decode('utf-8'))
s.send(b'exit')
s.close()