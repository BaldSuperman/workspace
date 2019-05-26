import threading
import time

class MyThread(threading.Thread):
    #必须定义run方法，线程执行的是run方法里的内容
    def run(self):
        for i in range(3):
            time.sleep(1)
            print(threading.currentThread())

if __name__ == '__main__':
    t = MyThread()
    t.start()
    print(threading.currentThread())