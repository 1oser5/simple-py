#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_SMTP.py
@Time    :   2019/01/05 12:32:03
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
# msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')

#发送html邮件
# msg = MIMEText('<html><body><h1>Hello</h1>' +
#     '<p>send by <a href="http://www.python.org">Python</a>...</p>' +
#     '</body></html>', 'html', 'utf-8')

#携带附件发送
msg = MIMEMultipart()
# 邮件正文是MIMEText:
msg.attach(MIMEText('send with file...', 'plain', 'utf-8'))
# 添加附件就是加上一个MIMEBase，从本地读取一个图片:
with open('/Users/xtl/Desktop/桌面.jpg', 'rb') as f:
    # 设置附件的MIME和文件名，这里是png类型:
    mime = MIMEBase('image', 'jpg', filename='test.jpg')
    # 加上必要的头信息:
    mime.add_header('Content-Disposition', 'attachment', filename='test.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    # 把附件的内容读进来:
    mime.set_payload(f.read())
    # 用Base64编码:
    encoders.encode_base64(mime)
    # 添加到MIMEMultipart:
    msg.attach(mime)

#输入Email地址和口令
from_addr = input('From: ')
password = input('password: ')
#输入收件人地址:
to_addr = input('To: ')
#输入SMTP服务器地址:
# smtp_server = input('SMTP server: ')
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
import smtplib
#加密smtp
smtp_server = 'smtp.gmail.com'
#gmail安全端口
smtp_port = 587
server = smtplib.SMTP(smtp_server, smtp_port)#默认端口为25
#创建安全连接
server.starttls()
#打印出所有交互信息
server.set_debuglevel(1)
#登录SMTP服务器
server.login(from_addr, password)
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()