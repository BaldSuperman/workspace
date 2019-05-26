import gevent
import time
#遇到延时函数就切换
#如果是用gevent则代码中的延时函数都需要使用gevent中的函数
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #time.sleep(0.5)
        gevent.sleep(0.5)
def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #time.sleep(0.5)
        gevent.sleep(0.5)
def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        #time.sleep(0.5)
        gevent.sleep(0.5)
g1 = gevent.spawn(f1, 5)# spawn(函数名，参数)
g2 = gevent.spawn(f2, 5)
g3 = gevent.spawn(f3, 5)
g1.join()
g2.join()
g3.join()