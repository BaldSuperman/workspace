import socket
import re
import multiprocessing
class WSGIServer(object):
    def __init__(self):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 在四次挥手时如果是服务器先结束，网页不会出问题
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定
        self.tcp_server_socket.bind(("127.0.0.1", 7900))
    def  service_client(self,new_socket):
        '''为这个客户端返回数据'''
        #接受浏览器发送的请求，即http请求
        #GET /HTTP/1.1
        print("*" * 50)
        requet = new_socket.recv(1024).decode("utf-8")
        #print(requet)
        # 将request得到的内容按照行进行切割为列表
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

    def run_forever(self):
        print("start*********")
        #创建套接字

        # 变为监听套接字
        self.tcp_server_socket.listen(128)
        #等待客户端链接
        while True:
            new_socket,client_addr = self.tcp_server_socket.accept()

            # 为这个客户端服务
            p = multiprocessing.Process(target=self.service_client, args=(new_socket,))
            p.start()
            new_socket.close()
        #关闭监听套接字
        self.tcp_server_socket.close()

def main():
    '''控制整体，创建一个web服务器对象,然后调用这个对象的run——forver方法运行'''
    wsgi_server = WSGIServer()
    wsgi_server.run_forever()
if __name__ == '__main__':
    main()