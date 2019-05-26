
import threading
from time import sleep
#定义一个全局变量
g_num = [100, 300]

def test1(num):
    num.append(33)
    num = str(num)
    print("test1 g_num: {0}".format(num))
def test2(num):
    num = str(num)

    print("test2 g_num: {0}".format(num))
def main():
    #target指定将来这个线程去那个函数执行代码
    #args指定将来调用函数的时候传递什么数据过去
    t1 = threading.Thread(target=test1, args=(g_num, ))
    t2 = threading.Thread(target=test2, args=(g_num, ))
    t1.start()
    sleep(1)
    t2.start()
    sleep(1)
    print("main :{0}".format(g_num))


if __name__ == '__main__':
    main()