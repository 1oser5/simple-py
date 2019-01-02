#!/usr/bin/env python3
import os
# print('Process (%s) is start'%os.getpid())
# pid = os.fork()
# #判断是否为子线程
# if pid ==0:
#     print('im %s ,my child is %s'%(os.getppid(),os.getpid()))
# else:
#     print('im %s ,my child is %s'%(os.getpid(),pid))


#使用mutleprocess调用多线程
from multiprocessing import Process,Pool
#设置子线程代码
# def run_proc(name):
#     print('Run child-process %s(%s)'%(name,os.getpid()))
# if __name__ == '__main__':
#     print('Parents process %s'%os.getpid())
#     p = Process(target = run_proc,args=('test',))
#     print('Child process will start')
#     p.start()
#     p.join()
#     print('Child process end')

#使用pool
import time,random
def long_time_task(name):
    print('Run task %s (%s)...'%(name,os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds'%(name,end-start))

if __name__ == '__main__':
    print('parent process %s start'%os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task,args=(i,))
    print('wait all subProcess done')
    p.close()
    p.join()
    print('done')
    

