import socket
import re
import threading
def  service_client(new_socket):
    '''为这个客户端返回数据'''
    #接受浏览器发送的请求，即http请求
    #GET /HTTP/1.1
    print("*" * 50)
    requet = new_socket.recv(1024).decode("utf-8")
    #print(requet)
    # 将request得到的内容进行切割为列表
    request_lines = requet.splitlines()
    print(request_lines)
    #得到的request_lines[0]的请求网页名字
    #get，post，put，del
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    if ret:
        files_name = ret.group(1)
        print(files_name)




    # - 准备发送给浏览器的数据。。。body,打开文件
    # response += "<h1>woshi ge shuage </>"

    try:
        f = open("D:/demo" + files_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUNT\r\n"
        response +="\r\n"
        response +="------file not fount-------"
        # 将response头发给浏览器
        new_socket.send(response.encode("utf-8"))
    else:
        html_contex = f.read()
        f.close()
        # 返回http格式的数据给浏览器
        # - 准备发送给浏览器的数据。。。header
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"
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
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #绑定
    tcp_server_socket.bind(("127.0.0.1", 7900))
    # 变为监听套接字
    tcp_server_socket.listen()
    #等待客户端链接
    while True:
        new_socket,client_addr = tcp_server_socket.accept()
        # 为这个客户端服务
        p = threading.Thread(target=service_client, args=(new_socket,))
        p.start()
        #new_socket.close()
    #关闭监听套接字
    tcp_server_socket.close()


if __name__ == '__main__':
    main()