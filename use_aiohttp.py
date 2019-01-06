#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   use_aiohttp.py
@Time    :   2019/01/06 13:43:42
@Author  :   William Xia
@Version :   1.0
@Contact :   snoopy98@163.com
@License :   (C)Copyright 2018-2019, HB.Company
@Desc    :   None
'''

# here put the import lib
import asyncio
from aiohttp import web

async def index(request):
    return web.Response(body = '<h1>Index</h1>'.encode(),content_type = 'text/html')

async def hello(request):
    text = '<h1>hello, %s1</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))

async def init(loop):
    app = web.Application(loop = loop)
    app.router.add_route('GET','/',index)
    app.router.add_route('GET','/hello/{name}',hello)
    srv = await loop.create_server(app.make_handler(),'127.0.0.1',8000)
    print('Server started at http://127.0.0.1:8000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()