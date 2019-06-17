# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc522



def write():
    reader = rc522()
    try:
        data = raw_input("input data: ")
        print("input data is: "+data)
        print("place your card to write")
        reader.write(data)
        print("write success")
        return data
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
    print("输入数字 1 查看当前卡内余额。",end=" ")
    print("*", end=" ")
    print("输入数字 2 管理员给当前卡片充值",end=" ")
    print("*", end=" ")
    print("输入数字 3 进行消费")

def judge4( Rfid):
    id, data = read()
    Rfid[id] = data
    print("当前组内成员：")
    for id in Rfid:
        print("id: " + str(id) + " data:" + str(Rfid[id]))
def judge1(Rfid):
    id, data = read()
    if id in Rfid.keys():
        print("id: " + str(id) + " data:" + str(Rfid[id]))
    else:
        print("不是我们的卡，没有相关权限")
def judge3(Rfid):
    id, data = read()
    if id in Rfid.keys():
        data = write()
        Rfid[id] = data
    else:
        print("不是我们的卡，没有相关权限")
def judge2(Rfid):
    count = len(Rfid)
    print("当前系统中共有卡片：%d 个"%count)
    for id in Rfid:
        print("id: " + str(id) + " data:" + str(Rfid[id]))
def judge(num, passwrod, Rfid):


    if num == '4':
        str = raw_input("请输入管理员密码：")
        if str == passwrod:
            judge4(Rfid)
        else:
            print("您没有相关权限")
    if num == '3':
        str = raw_input("请输入管理员密码：")
        if str == passwrod:
            judge3(Rfid)
        else:
            print("您没有相关权限")
    if num == '2':
        str = raw_input("请输入管理员密码：")
        if str == passwrod:
            judge2(Rfid)
        else:
            print("您没有相关权限")
    if num == '1':
        judge1(Rfid)


def main():

    passwrod = "xiamingxin"
    ##使用字典代替数据库功能 存储当前组内卡片信息

    while True:
        show()
        num = raw_input("输入您的操作类型：")
        judge(num, passwrod, Rfid)

if __name__ == '__main__':
    main()

