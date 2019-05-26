import socket

def tcp_srv():
    '''
    建立socket负责具体通信，这个socke其实只负责接受对方的请求
    需要2个参数
    socket.AF_INET:含义与UDP相同
    socket.SOCK_STREam:表明是使用的tcp通信

    '''
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #绑定端口和地址
    #此地址类型是个元组类型，第一部分为字符串，代表ip，第二部分为端口
    addr = ("127.0.0.1", 8998)
    sock.bind(addr)
    #监听接入的访问socket
    sock.listen()
    while True:
        # 接受访问的socket，可以理解接受访问即建立了一个通讯的链接通路
        #accept返回元组第一个元素复制给skt，第二个个addr
        skt,addr = sock.accept()
        #接受对方发送的内容，利用接受到的socket接受内容
        #500表示接受使用的buffersize

        msg = skt.recv(500)
        #接受到的是bytes格式内容
        #想得到str格式的，需要解码
        msg = msg.decode()
        rst = "RECEIVED msg:{0},from{1}".format(msg, addr)
        print(rst)
        #如果有必要给对方发送反馈消息
        skt.send(rst.encode())
        skt.close()
if __name__ == '__main__':
    print("start****")
    tcp_srv()
    print("”end***")