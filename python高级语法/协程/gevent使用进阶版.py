import gevent
import time
from gevent import monkey
#使用gevent时遇到延时函数就切换
#如果是用gevent则代码中的延时函数都需要使用gevent中的函数
#如果不想修改所有函数的代码，可以使用补丁
monkey.patch_all()
 #所有延时操作的代码，全部使用gevent里面的代码
def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)

#g1 = gevent.spawn(f1, 5)# spawn(函数名，参数)
#g2 = gevent.spawn(f2, 5)
#g3 = gevent.spawn(f3, 5)
#g1.join()
#g2.join()
#g3.join()
#将创建的gevent放入joinall列表中意味着等待所有的都结束
gevent.joinall([
    gevent.spawn(f1, 5),# spawn(函数名，参数)
    gevent.spawn(f2, 5),
    gevent.spawn(f3, 5),
])