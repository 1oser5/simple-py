def fn(self,name = 'world'):
    print('Hello,%s'%name)
#使用type定义类
Hello = type('Hello',(object,),{hello:fn,})
h =Hello()
h.hello('mac')