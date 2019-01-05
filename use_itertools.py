#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_itertools.py
@Time    :   2019/01/02 14:30:47
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import itertools

#无限循环
# nautals = itertools.count(1)
# for n in nautals:
#     print(n)

#序列循环
# cs = itertools.cycle('ABC')
# for c in cs:
#     print(c)
# A
# B
# C
# A
# B
# C

#重复元素，可以限定次数
# ns = itertools.repeat('A',3)
# for n in ns:
#     print(n)

#使用takewhile()函数取出
# natuals = itertools.count(2)
# ns = itertools.takewhile(lambda x:x<=10,natuals)
# print(list(ns))

#chain将迭代对象串联起来
# for c in itertools.chain('ABC','XYZ'):
#     print(c)

#groupby将相邻并且相同元素抽取
# for key,group in itertools.groupby('aaaBBBAAACCAAbbAAAaa'):
#     print(key, list(group))
from functools import reduce
#计算pi值
def pi(N):
    count = 0
    cs = itertools.cycle([4,-4])
    ns = itertools.count(1,2)
    result  = itertools.takewhile(lambda x: x<=2*N-1,ns)
    result = map(lambda x: next(cs)/x,result)
    return reduce(lambda x,y:x+y,result)
# 测试:
print(pi(10))
print(pi(100))
print(pi(1000))
print(pi(10000))
assert 3.04 < pi(10) < 3.05
assert 3.13 < pi(100) < 3.14
assert 3.140 < pi(1000) < 3.141
assert 3.1414 < pi(10000) < 3.1415
print('ok')