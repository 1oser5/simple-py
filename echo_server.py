#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   echo_server.py
@Time    :   2019/01/04 15:23:48
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import socket,threading,time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 监听端口:
s.bind(('127.0.0.1',9999))
s.listen(5)
print('Waiting for connection...')
def tcplink(sock, addr):
    print('Accept new connection from')
    sock.send(b'Welcome')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if not data or data.decode('utf-8') == 'exit':
            break
        sock.send(('Hello,%s'%data.decode('utf-8')).encode('utf-8'))
    sock.close()
while True:
    #接受一个新的连接
    sock, addr = s.accept()
    #创建新线程来处理tcp连接:
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
    print('Connection from %s:%s closed.' % addr)

