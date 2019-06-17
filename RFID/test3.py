# -*- coding: utf-8 -*-
import socket
"""
        1. 建立通信的socket
        2. 发送内容到指定服务器
        3. 接受服务器给定的反馈内容
"""
import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522 as rc522



import RPi.GPIO
import time
import datetime

GPIO_DHT11 = 20

SLEEP_SECOND = 2
LED_OPENED = True

RPi.GPIO.setmode(RPi.GPIO.BCM)


def setupDHT11():
    RPi.GPIO.setup(GPIO_DHT11, RPi.GPIO.OUT)
    RPi.GPIO.output(GPIO_DHT11, RPi.GPIO.LOW)
    time.sleep(0.02)
    RPi.GPIO.output(GPIO_DHT11, RPi.GPIO.HIGH)
    RPi.GPIO.setup(GPIO_DHT11, RPi.GPIO.IN)
def read():
    data = []

    while RPi.GPIO.input(GPIO_DHT11) == RPi.GPIO.LOW:
        continue
    while RPi.GPIO.input(GPIO_DHT11) == RPi.GPIO.HIGH:
        continue
    j = 0
    while j < 40:
        print("reader")
        k = 0
        while RPi.GPIO.input(GPIO_DHT11) == RPi.GPIO.LOW:
            continue
        while RPi.GPIO.input(GPIO_DHT11) == RPi.GPIO.HIGH:
            k += 1
            if k > 100:
                break
        if k < 8:
            data.append(0)
        else:
            data.append(1)
        j += 1
    return data

def checkData(data):
    global LED_OPENED
    humidity_bit = data[0:8]
    humidity_point_bit = data[8:16]
    temperature_bit = data[16:24]
    temperature_point_bit = data[24:32]
    check_bit = data[32:40]
    humidity = 0
    humidity_point = 0
    temperature = 0
    temperature_point = 0
    check = 0
    for i in range(8):
        humidity += humidity_bit[i] * 2 ** (7-i)
        humidity_point += humidity_point_bit[i] * 2 ** (7-i)
        temperature += temperature_bit[i] * 2 ** (7- i)
        temperature_point += temperature_point_bit[i] * 2 ** (7-i)
        check += check_bit[i] * 2 ** (7-i)
    tmp = humidity + humidity_point + temperature + temperature_point
    if check == tmp:
        if not LED_OPENED:

          print(" got right data now, open the LED")
          LED_OPENED = True
        print("temperature :[0] C, humidity :{1} %%".format( temperature, humidity))
        return temperature, humidity
    if LED_OPENED:
         print("got wrong data now, close the LED")

         LED_OPENED = False
    return None, None
def tcp(sock):

    # 链接对方，请求根对方建立通路

    print("time: " + str(datetime.datetime.now()))

    data = read()

    temperature, humidity = checkData(data)
    text = "<div>当前温度：{0}</div><div>当前湿度：{1}</div>".format(temperature, humidity)
    print("text")
    data = text.encode()
    # 发送
    sock.sendto(data)



    rst = sock.recv(5000)

    print(rst.decode())
    # 关闭链接通路
    sock.close()
def rfid(sock):
    print("请刷卡")
    reader = rc522()
    try:

        id, data = reader.read()
        print("id is " + str(id))
        print("data is " + str(data))
        data = int(data)-2
        data = str(data)
        reader.write(data)
        tcp(sock)

    except Exception as error:
        print("error haappen: " + str(error))
    finally:
        GPIO.cleanup()


if __name__ == '__main__':
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ("192.168.1.108", 8948)
    sock.connect(addr)
    setupDHT11()
    while True:
        print("****")
        rfid(sock)

