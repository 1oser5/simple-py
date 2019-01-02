#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   do_time.py
@Time    :   2019/01/01 17:54:02
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib

from datetime import datetime,timedelta
#获取当前时间
now = datetime.now()

#获取指定时间
dt = datetime(2015,3,21,12,10)
#2015-03-21 12:10:00

#datetime转换为timestamp
dt = datetime(2015, 4, 19, 12, 20) # 用指定日期时间创建datetime
dt.timestamp() # 把datetime转换为timestamp
#注意Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数
#js则是毫秒

#timestamp转换为datetime
t = 1429417200.0
datetime.fromtimestamp(t)
#timestamp也可以直接被转换到UTC标准时区的时间：
datetime.utcfromtimestamp(t)

#str转换为datetime
cday = datetime.strptime('2015-6-1 18:19:59', '%Y-%m-%d %H:%M:%S')
#2015-06-01 18:19:59

#datetime转换为str
now = datetime.now()
now.strftime('%a, %b %d %H:%M')
# Mon, May 05 16:28

#datetime加减
datetime.datetime(2015, 5, 18, 16, 57, 3, 540997)
now + timedelta(hours=10)