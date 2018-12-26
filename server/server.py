#引入wsgiref模块
from wsgiref.simple_server import make_server
#导入api函数
from api import application

#创建服务器，ip地址为空，端口号为8000，处理函数为application
https = make_server('',8000,application)
print('serving HTTP on port 8000..')

#开始监听
https.serve_forever()