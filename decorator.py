import time, functools


def metric(fn):
    beforeTime = time.time()
    @functools.wraps(fn)
    def wrapper(*args,**kw):
        print('%s executed in %s ms' % (fn.__name__,time.time()-beforeTime))
        return fn(*args,**kw)
    return wrapper

# @metric
# def fast(x, y):
#     time.sleep(0.0012)
#     return x + y;

# @metric
# def slow(x, y, z):
#     time.sleep(0.1234)
#     return x * y * z;

# f = fast(11, 22)
# s = slow(11, 22, 33)
# if f != 33:
#     print('测试失败!')
# elif s != 7986:
#     print('测试失败!')

def log(params):
    if isinstance(params,str):
        def metric(fuc):
            def wrapper(*args,**kw):
                print(params)
                print('start')
                fuc(*args,**kw)
                print('end')
            return wrapper
        return metric
    else:    
        def wrapper(*args,**kw):
            print('start')
            params(*args,**kw)
            print('end')
        return wrapper
@log('excute')
def f():
    pass
f()