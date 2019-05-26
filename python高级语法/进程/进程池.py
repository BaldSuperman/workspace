from multiprocessing import Pool
import time,os
def task(name):
    start = time.time()
    print('name',name)
    time.sleep(1)
    end = time.time()

    print("耗时 :{0}，进程号: {1}".format(end-start, os.getpid()))
if __name__ == '__main__':
    po = Pool(3)#创建容量为3进程池

    for i in range(10):
      po.apply_async(task, (i,))

    po.close()#join函数必须写在close后面
    po.join()
    print('主')

