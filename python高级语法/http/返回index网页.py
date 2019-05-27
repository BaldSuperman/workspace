import socket

def  service_client(new_socket):
    '''为这个客户端返回数据'''
    #接受浏览器发送的请求，即http请求
    #GET /HTTP/1.1

    requet = new_socket.recv(1024)
    print(requet)
    #返回http格式的数据给浏览器
    # - 准备发送给浏览器的数据。。。header
    response = "HTTP/1.1 200 OK \r\n"
    response += "\r\n"
    print("*"*20)
    # - 准备发送给浏览器的数据。。。body,打开文件
    # response += "<h1>woshi ge shuage </>"
    with open(r"D:/demo/index.html", "rb") as f:
        html_contex = f.read()
    # 将response头发给浏览器
    new_socket.send(response.encode("utf-8"))
    # 将responsebody发给浏览器
    new_socket.send(html_contex)
    # 关闭套接字
    new_socket.close()

def main():
    print("start*********")
    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定
    tcp_server_socket.bind(("127.0.0.1", 7900))
    # 变为监听套接字
    tcp_server_socket.listen(128)
    #等待客户端链接
    while True:
        new_socker,client_addr = tcp_server_socket.accept()
        # 为这个客户端服务
        service_client(new_socker)



if __name__ == '__main__':
    main()