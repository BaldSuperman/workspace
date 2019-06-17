import socket
import re
import threading
def  service_client2(new_socket,tcp_text):
    '''为这个客户端返回数据'''
    #接受浏览器发送的请求，即http请求
    #GET /HTTP/1.1
    requet = new_socket.recv(1024).decode("utf-8")
    request_lines = requet.splitlines()
    print(request_lines)
    # 得到的request_lines[0]的请求网页名字
    # get，post，put，del
    ret = re.match(r"[^/]+(/[^ ]*)", request_lines[0])
    html_1 = """
           <div>当前付费状态：未付费</div>
           <div>当前温度：未知</div>
           <div>当前湿度：未知</div>"""
    print(tcp_text)
    if ret:
        files_name = ret.group(1)
        print(files_name)
    try:
        f = open("D:\python_work\RFID" + files_name, "rb")
    except:
        response = "HTTP/1.1 404 NOT FOUNT\r\n"
        response +="\r\n"
        response +="------file not fount-------"
        # 将response头发给浏览器
        new_socket.send(response.encode("utf-8"))
    else:
    #返回http格式的数据给浏览器
    # - 准备发送给浏览器的数据。。。header
        response = "HTTP/1.1 200 OK \r\n"
        response += "\r\n"

        # - 准备发送给浏览器的数据。。。body,打开文件
        # response += "<h1>woshi ge shuage </>"

        html_contex = f.read()
        num = len(tcp_text)-1
        ch = tcp_text[num]

        html_contex = re.sub(html_1, ch, html_contex.decode('utf-8'))
        # 将response头发给浏览器
        response +="\r\n"
        response += html_contex
        print(response)
        new_socket.send(response.encode("utf-8"))
        # 将responsebody发给浏览器

    # 关闭套接字
    new_socket.close()
def  service_client1(new_socket,tcp_text):
    '''为这个客户端返回数据'''
    #接受浏览器发送的请求，即http请求
    #GET /HTTP/1.1

    print("*2" * 50)
    requet = new_socket.recv(1024).decode("utf-8")
    #print(requet)
    # 将request得到的内容进行切割为列表

    print(requet)
    #得到的request_lines[0]的请求网页名字
    #get，post，put，del

    if requet:
    # - 准备发送给浏览器的数据。。。body,打开文件
    # response += "<h1>woshi ge shuage </>"
        html = "<div>当前付费状态：已付费</div>"+requet


        tcp_text.append(html)
        print(tcp_text)
    # 关闭套接字
    new_socket.close()

def main():
    tcp_ip = list()
    tcp_text = list()
    html_1 = """
              <div>当前付费状态：未付费</div>
              <div>当前温度：未知</div>
              <div>当前湿度：未知</div>"""
    tcp_text.append(html_1)
    print("start*********")
    #创建套接字
    tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #绑定
    tcp_server_socket.bind(("192.168.1.108", 8948))
    # 变为监听套接字
    tcp_server_socket.listen()
    #等待客户端链接

    new_socker, client_addr = tcp_server_socket.accept()
    p = new_socker
    p = threading.Thread(target=service_client1, args=(p, tcp_text))
    p.start()
    while True:

        new_socker, client_addr = tcp_server_socket.accept()
        if str(new_socker) == "192.168.1.106":
            p = threading.Thread(target=service_client2, args=(new_socker, tcp_text))
        # 为这个客户端服务
        else:
            p = threading.Thread(target=service_client2, args=(new_socker,tcp_text))
            p.start()
    tcp_server_socket.close()




if __name__ == '__main__':
    main()