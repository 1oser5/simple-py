#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import threading
#创建全局local对象
local_student = threading.local()

def process_student():
  
  #获得相关线程的student:
    std = local_student.student
    print('Hello, %s (in %s)'%(std,threading.current_thread().name))

def process_thread(name):
    #绑定threadLocal的student
    local_student.student = name
    process_student()

t1 = threading.Thread(target= process_thread, args=('Alice',), name = 'Thread-A')
t2 = threading.Thread(target= process_thread, args=('Bob',), name = 'Thread-B')
t1.start()
t2.start()
t1.join()
t2.join()