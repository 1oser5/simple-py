#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_POP3.py
@Time    :   2019/01/05 16:13:52
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import poplib
from email.parser import Parser 
#输入邮箱地址,口令和pop3服务器地址:
email = input('Email: ')
password = input('Password: ')
pop3_server = input('POP3 server: ')

#连接到pop3服务器:
server = poplib.POP3(pop3_server)
#可以开始或关闭调试信息:
server.set_debuglevel(1)
#可选，打印pop3服务器的欢迎文字:
print(server.getwelcome().decode('utf-8'))

#身份认证:
server.user(email)
server.pass_(password)

#start()返回邮箱数量和占用空间:
print('Message: %s.Size: %s'% server.stat())
#list()返回所有邮件的编号:
resp, mails, octets = server.list()
#可以查看返回的列表类似[b'1',b'2']
print(mails)

#获得最新一封邮件，注意所以会从1开始:
index = len(mails)
resp, lines, octets = server.retr(index)

#lines储存了邮件的原始文本的每一行
#可以获得整个邮件的原始文件:
msg_content = b'\r\n'.join(lines).decode('utf-8')
#解析出邮件:
msg = Parser().parsestr(msg_content)

#可以根据邮件索引号直接从服务器删除邮件:
#server.dele(index)
#关闭连接:
server.quit()

##解析邮件
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

