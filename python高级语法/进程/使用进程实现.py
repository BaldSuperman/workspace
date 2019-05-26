import threading
from time import sleep
import multiprocessing

from time import sleep
#定义一个全局变量


def test1():
    while True:
        print("1*********")
        sleep(1)
def test2():
    while True:
        print("2*********")
        sleep(1)


def main():
    #target指定将来这个线程去那个函数执行代码
    #args指定将来调用函数的时候传递什么数据过去
    t1 = multiprocessing.Process(target=test1,)
    t2 = multiprocessing.Process(target=test2, )
    t1.start()

    t2.start()




if __name__ == '__main__':
    main()