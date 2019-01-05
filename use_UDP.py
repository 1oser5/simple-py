#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_UDP.py
@Time    :   2019/01/05 12:11:27
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import socket
##服务端
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#绑定端口:
s.bind(('127.0.0.1', 9999))
print('Bind UDP on 9999...')
while True:
    #接收数据:
    data, addr = s.recvfrom(1024)
    print('Received from %s:%s.' % addr)
    s.sendto(b'Hello,%s!' %data, addr)

##客户端
c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for data in [b'Alice', b'Bob', b'Client']:
    #发送数据:
    s.sendto(data,('127.0.0.1',9999))
    #接受数据:
    print(s.recv(1024).decode('utf-8'))
s.close()