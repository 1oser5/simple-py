from functools import reduce

##序列化
# def normalize(name):
#     return name[:1].upper()+name[1:].lower()
# name = ['adam', 'LISA', 'barT']
# r = map(normalize,name)
# print(list(r))

##reduce求和
# L1 = [1,2,3,4,5,6]
# def prod(L):
#     def multiply(x,y):
#         return x * y
#     return reduce(multiply,L)
# print(prod(L1))


##二进制转换
# def str2float(s):
#     i = s.find('.')
#     if i!=-1:
#         return reduce(lambda x,y:(10*x)+y,map(int,s[:i]))+reduce(lambda x,y:(10*x)+y,map(int,s[i+1:]))
#     else:
#         return reduce(lambda x,y:(10*x)+y,map(int,s))
# print(str2float('123.123'))

def str2float(s):
    i=s.find('.') #找到小数点
    s1, s2 = list(map(int, s[:i])), list(map(int, s[i+1:]))
    ##字符串倒序
    print(s2[::-1])
    r1, r2 = reduce(lambda x, y: 10*x+y, s1), reduce(lambda x, y: 0.1*x+y, s2[::-1])*0.1
    return r1+r2  
print(str2float('123.123'))
