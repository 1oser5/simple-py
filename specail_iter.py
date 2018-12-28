class Fib(object):
    def __init__(self):
        self.a,self.b = 0 ,1

    ##实现迭代
    def __iter__(self):
        return self#实例本身就是迭代对象，顾只需返回值
    def __next__(self):
        self.a,self.b=self.b,self.a+self.b
        if self.a>1000:
            raise StopIteration()
        return self.a
    #实现下标提取元素,或者切片函数
    def __getitem__(self,n):
        if isinstance(n,int):
            a,b=1,1
            for index in range(n):
                a,b = b,a+b
            return a
        else:
            L=[]
            start = n.start if n.start !=None else 0
            stop = n.stop
            a,b=1,1
            for n in range(stop):
                if(n>=start):
                    L.append(a)
                a,b = b,a+b
            return L
    ##动态设置属性
    def __getattr__(self,attr):
        if attr == 'big':
            return 99
        raise AttributeError('\'Studnet\' object has no attribute \'%s\' '%attr)

    def __call__(self):
        print('called')
                    
        

# for n in Fib():
#     print(n)
f=Fib()
# print(f.big)
f()
# print(f.small)


##通过getatter动态返回一个属性
class Chain(object):
    def __init__(self,path=''):
        self._path = path
    def __getattr__(self,path):
        return Chain('%s/%s'%(self._path,path))
    def __str__(self):
        return self._path
print(Chain().main.list.getAllList.file.lack)
    
