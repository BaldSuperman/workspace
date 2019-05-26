import socket
"""
        1. 建立通信的socket
        2. 发送内容到指定服务器
        3. 接受服务器给定的反馈内容
"""

def cilentFunc():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "yang"
    # 发送的数据必须是bytes格式
    data = text.encode()

    #发送
    sock.sendto(data,("127.0.0.1", 7852))

    #等待接受反馈
    data, addr = sock.recvfrom(200)
    #解码，默认utf-8
    data =data.decode()
    print(addr)

if __name__ == '__main__':
    print("发起")
    cilentFunc()
    print("结束")