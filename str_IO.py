from io import StringIO,BytesIO
#操作str
f=StringIO()
f.write('hello')
f.write('word')
print(f.getvalue())
#操作二进制数
b = BytesIO()
b.write('中国'.encode('utf-8'))
print(b.getvalue())
