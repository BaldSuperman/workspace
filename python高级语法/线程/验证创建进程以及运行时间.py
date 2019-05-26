#enumerate 返回一个包含正在运行的线程list
#结论：只有start之后才会创建线程，以及运行线程
import threading
import time

def test1():
   for i in range(5):
        print("test1     *****{0}".format(i))

    #如果创建Thread时执行的函数，运行结束意味着这个子线程结束了


def main():
    #在调用Thread之前先打印当前线程信息
    print(threading.enumerate())

    t1 = threading.Thread(target=test1)#target是函数名不能加括号
    #在调用Thread之后调用
    print(threading.enumerate())
    t1.start()
    #在start之后
    print(threading.enumerate())
if __name__ == '__main__':
    main()
