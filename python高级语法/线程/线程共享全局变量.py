
import threading
from time import sleep
#定义一个全局变量
g_num =100

def test1():
    global g_num
    g_num +=1
    print("test1 g_num: {0}".format(g_num))
def test2():
    print("test2 g_num: {0}".format(g_num))
def main():
    t1 = threading.Thread(target=test1)
    t2 = threading.Thread(target=test2)
    t1.start()
    sleep(1)
    t2.start()
    sleep(1)
    print("main :{0}".format(g_num))


if __name__ == '__main__':
    main()