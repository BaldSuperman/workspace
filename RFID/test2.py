import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc522



def write():
    reader = rc522()
    try:
        id,data1 = reader.read()
        data = raw_input("input data: ")
        print("input data is: "+(data))
        print("place your card to write")
        data1 = int(data1) + int(data)
        data1 = str(data1)
        reader.write(data1)
        print("write success")
        return data1
    except Exception as error:
        print("error haappen: "+str(error))
    finally:
        GPIO.cleanup()
def write1():
    reader = rc522()
    try:
        id,data1 = reader.read()
        data = '30'
        print("input data is: "+str(data))
        print("place your card to write")
        data1 = int(data1)-int(data)
        data1 = str(data1)
        reader.write(data1)
        print("write success")
        return data1
    except Exception as error:
        print("error haappen: "+str(error))
    finally:
        GPIO.cleanup()
def read():
    reader = rc522()
    try:
        print("begin reading")
        id, data = reader.read()
        return id, data
    except Exception as error:
        print("error haappen:%s" % str(error))
    finally:
        GPIO.cleanup()
def show():
    print("输入数字 1 查看当前卡内余额。")

    print("输入数字 2 管理员给当前卡片充值")

    print("输入数字 3 进行消费(每次查询30圆)")


def judge1():
    id, data = read()

    print("id: " + str(id) + " data:" + str(data))

def judge2():
    id, data = read()
    print("id: " + str(id) + " 当前余额data:" + str(data))
    data = write()
    print("id: " + str(id) + " 当前余额data:" + str(data))

def judge3():
    id, data = read()
    print("id: " + str(id) + " 当前余额data:" + str(data))
    data = write1()
    print("id: " + str(id) + " 当前余额data:" + str(data))
def judge(num, passwrod):

    if num == '3':
        str = raw_input("请输入管理员密码：")
        if str == passwrod:
            judge3()
        else:
            print("您没有相关权限")
    if num == '2':
        str = raw_input("请输入管理员密码：")
        if str == passwrod:
            judge2()
        else:
            print("您没有相关权限")
    if num == '1':
        judge1()


def main():

    passwrod = "yang"
    ##使用字典代替数据库功能 存储当前组内卡片信息

    while True:
        show()
        num = raw_input("输入您的操作类型：")
        judge(num, passwrod)

if __name__ == '__main__':
    main()
