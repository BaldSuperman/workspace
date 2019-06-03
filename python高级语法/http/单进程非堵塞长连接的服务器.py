import socket
import re
import gevent
from gevent import monkey
import time

'''

tcp_server_tcp.setblocking(False) 设置套接字为非堵塞方式
'''
monkey.patch_all()
def  service_client(new_socket, request):
    '''为这个客户端返回数据'''
    #接受浏览器发送的请求，即http请求
    #GET /HTTP/1.1
    print("*" * 50)
   # requet = new_socket.recv(1024).decode("utf-8")
    #print(requet)
    # 将request得到的内容进行切割为列表
    request_lines = request.splitlines()
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
        response_body = html_contex
        response_header = "HTTP/1.1 200 OK \r\n"
        response_header += "Content-Length:%d\r\n" % len(response_body)
        response_header += "\r\n"

        response = response_header.encode("utf-8") + response_body


        # 将response头发给浏览器
        new_socket.send(response)

    # 关闭套接字
    # new_socket.close()#不执行new_socket.close()意思是使用长连接

def main():
    print("start*********")
    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #绑定
    tcp_server_socket.bind(("127.0.0.1", 7900))
    # 变为监听套接字
    tcp_server_socket.listen()
    #创建一个保存接受到消息的列表，使用for循环判断是否有信息
    client_socket_list = list()
    tcp_server_socket.setblocking(False)#设置套接字为非堵塞方式
    #等待客户端链接
    while True:
        '''
        new_socket,client_addr = tcp_server_socket.accept()
        # 为这个客户端服务
        gevent.spawn(service_client, new_socket)
        '''
        time.sleep(1)
        try:
            new_socket,client_addr = tcp_server_socket.accept()
        except Exception as ret :
            #print("没有新的客户端到来")
            pass
        else:
            #print("来了新的客户端")
            new_socket.setblocking(False)
            client_socket_list.append(new_socket)
        for client_socket in client_socket_list:
            try:
                recv_data = client_socket.recv(1024).decode("utf-8")
            except Exception as ret:
                #print("这个客户端没有发来数据")
                pass
            else:
                if recv_data:
                    #对方发过来数据
                    #print("发了数据")
                    service_client(client_socket, recv_data)
                else:
                    client_socket.close()
                    client_socket_list.remove(client_socket)


if __name__ == '__main__':
    main()