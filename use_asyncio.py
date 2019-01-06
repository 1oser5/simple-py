#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_asyncio.py
@Time    :   2019/01/06 11:59:15
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import asyncio,threading

# @asyncio.coroutine
# def hello():
#     print('Hello world! (%s)' % threading.currentThread())
#     #异步调用asyncio.sleep(1)
#     yield from asyncio.sleep(1)
#     print('Hello again! (%s)' % threading.currentThread())
# #获取event_loop流
# loop = asyncio.get_event_loop()
# tasks = [hello(), hello()]
# #执行coroutine
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

# @asyncio.coroutine
# def wget(host):
#     print('wget %s...' % host)
#     connect = asyncio.open_connection(host, 80)
#     reader, writer = yield from connect
#     header = 'GET / HTTP/1.0\r\nHost: %s\r\n\r\n' % host
#     writer.write(header.encode('utf-8'))
#     yield from writer.drain()
#     while True:
#         line = yield from reader.readline()
#         if line == b'\r\n':
#             break
#         print('%s header > %s' % (host, line.decode('utf-8').rstrip()))
#         # Ignore the body, close the socket
#     writer.close()
# #获取线程
# loop = asyncio.get_event_loop()
# tasks = [wget(host) for host in ['www.baidu.com', 'www.sohu.com', 'www.163.com']]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()


# Python从3.5版本开始为asyncio提供了async和await的新语法
async def hello():
    print('Hello world! (%s)' % threading.currentThread())
    #异步调用asyncio.sleep(1)
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
#获取event_loop流
loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
#执行coroutine
loop.run_until_complete(asyncio.wait(tasks))
loop.close()