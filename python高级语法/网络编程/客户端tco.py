import socket

def tcp_clt():
    # 建立通信socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # 链接对方，请求根对方建立通路
    addr = ("127.0.0.1", 8998)
    sock.connect(addr)
    #发送内容到对方服务器
    msg = "hahah"
    sock.send(msg.encode())
    #接受对方的反馈
    rst = sock.recv(5000)

    print(rst.decode())
    #关闭链接通路
    sock.close()
if __name__ == '__main__':
    tcp_clt()