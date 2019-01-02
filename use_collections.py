#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_collections.py
@Time    :   2019/01/02 10:04:32
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
from collections import namedtuple,deque,defaultdict,OrderedDict

#namedtuple
Point = namedtuple('Point',['x','y'])
p = Point(1,2)
# print(p)

#deque
q = deque(['a','b','c'])
#首部加入
q.appendleft('a')
#尾部加入
q.append('x')
# print(q)
# deque(['a', 'a', 'b', 'c', 'x'])

#defaultdict
dd = defaultdict(lambda:'N/A')
dd['key'] = 'abc'
# print(dd['key'])
# print(dd['nokey'])
# abc
# N/A


#OrderedDict
d = dict([('a',1),('b',2),('c',3)])
# d = OrderedDict([('a',1),('b',3),('c',2)])
print(d)