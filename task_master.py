#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   task_master.py
@Time    :   2019/01/01 16:47:23
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2017-2018, HB.Company
@Desc    :   None
'''

# here put the import lib
import random,time,queue
from multiprocessing.managers import BaseManager
#发送任务的队列
task_queue = queue.Queue()
#接受任务的队列
result_queue = queue.Queue()
#继承BaseManager
class QueueManager(BaseManager):
    pass
#将两个queue注册在网上，callable关联了queue对象
QueueManager.register('get_task_queue',callable=lambda: task_queue)
QueueManager.register('get_result_queue',callable=lambda: result_queue)
# 绑定端口5000, 设置验证码'abc':
manager = QueueManager(address=('',5000),authkey=b'abc')
#启动queue
manager.start()
#通过网络访问queue对象
task = manager.get_task_queue()
result = manager.get_result_queue()
#放入任务
for i in range(10):
    n = random.randint(0,10000)
    print('Put task %d...' % n)
    task.put(n)
#从队列读取任务
print('Try get results...')
for i in range(10):
    r = result.get(timeout = 10)
    print('Result: %s' % r)
# 关闭:
manager.shutdown()
print('master exit.')