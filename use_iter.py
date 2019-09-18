#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_iter.py
@Time    :   2019/09/12 08:36:26
@Author  :   Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2019-2020, HB.Company
@Desc    :   None
'''

# here put the import lib
class test:
    def __init__(self,data):
        self.data = data
    
    def __iter__(self):
        print('use iter function')
        return self
    def __next__(self):
        print('use next function')
        if self.data > 5:
            raise StopIteration
        else:
            self.data += 1
            return self.data

if __name__ == '__main__':
    for item in test(3):
        print(item)
        