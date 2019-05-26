#enumerate 返回一个包含正在运行的线程list
import threading
import time

def test1():
   for i in range(5):
        print("test1     *****{0}".format(i))
        time.sleep(1)
    #如果创建Thread时执行的函数，运行结束意味着这个子线程结束了
def test2():
    for i in range(10):
        print("test2     *****{0}".format(i))
        time.sleep(1)

def main():
    t1 = threading.Thread(target=test1)#target是函数名不能加括号
    t2 = threading.Thread(target=test2)
    t1.start()

    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate() )<= 1:
            break
        time.sleep(1)
if __name__ == '__main__':
    main()
