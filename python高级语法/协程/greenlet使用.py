from greenlet import greenlet
import time
def test1():
    while True:
        print("------A----")
        gr2.switch()
        time.sleep(0.1)


def test2():
    while True:
        print("------B----")
        gr1.switch()
        time.sleep(0.1)


gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到grl中运行
gr1.switch()