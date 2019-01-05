#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_contextlib.py
@Time    :   2019/01/02 15:28:34
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib


#通过__enter__和__exit__实现上下文管理

# class Query(object):
#     def __init__(self,name):
#         self.name = name
#     def __enter__(self):
#         print('begin')
#         return self
#     def __exit__(self,exc_type, exec_value, trackback):
#         if exc_type:
#             print('Error')
#         else:
#             print('End')
#     def query(self):
#         print('Query info about %s'%self.name)
# with Query('Bob') as q:
#     q.query()


from contextlib import contextmanager
class Query(object):
    def __init__(self,name):
        self.name = name
    def query(self):
        print('Query info about %s'%self.name)

@contextmanager
def create_query(name):
    print('Begin')
    q = Query(name)
    yield q
    print('End')
# with create_query('Bob') as q:
#     q.query()

#更典型的例子:
@contextmanager
def tag(name):
    print('<%s>'%name)
    yield
    print('<%s>'%name)
with tag('h1'):
    print('hello')
    print('world')
    