import socket
import re
import multiprocessing
#import dynamic.mini_frame
import sys
class WSGIServer(object):
    def __init__(self, port, app, static_path):
        self.tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 在四次挥手时如果是服务器先结束，网页不会出问题
        self.tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        # 绑定

        self.tcp_server_socket.bind(("127.0.0.1", port))
        self.app = app
        self.static_path = static_path
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
        #判断请求的页面是否是.py结尾，如果是说明是动态资源
        #如果不是.py结尾，那么就认为是静态资源
        if not files_name.endswith(".py"):
        # - 准备发送给浏览器的数据。。。body,打开文件
        # response += "<h1>woshi ge shuage </>"
            try:
                f = open(self.static_path + files_name, "rb")
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
        else:
            #如果是以.py结尾，那么就认为是动态资源请求

            '''if files_name=="/login.py":
                body = mini_frame.login()
            elif files_name=="/register.py":
                body = mini_frame.register()'''
            #将
            env = dict()
            env["PATH_INFO"] = files_name
            #{PATH_INFO:files_name}
            #body = dynamic.mini_frame.application(env, self.set_resonse_header)
            body = self.app(env, self.set_resonse_header)

            header = "HTTP/1.1 %s OK\r\n"%self.status
            for temp in self.headers:
                header += "%s:%ls\r\n"%(temp[0],temp[1])
            header += "\r\n"

            response = header + body
            new_socket.send(response.encode("utf-8"))
        # 关闭套接字
        new_socket.close()
    def set_resonse_header(self, status,headers):
        self.status = status
        self.headers = [("server","mini web v0.9")]
        self.headers += headers
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
    if len(sys.argv) == 3:
        try :
            port = int(sys.argv[1])
            frame_app_name = sys.argv[2]
        except Exception as ret:
            print("端口输入错误")
            return
    else:
        print("请按照一下方式运行")
        print("python xxx.py 7899 mini_frame:application")
        return
    #将取出的frame_app_name进行切割
    ret = re.match(r"([^:]+):(.*)",frame_app_name)
    if ret:
        frame_name = ret.group(1)#拿到mini_frame
        app_name = ret.group(2)#拿到application
    else:
        print("请按照一下方式运行")
        print("python xxx.py 7899 mini_frame:application")

    with open(r"./web_serve.conf") as f:
        conf_info = eval(f.read())#将读取的数据更改为字典类型

    #将得到的需要使用的函数名进行导入
    #由于mini_frame 不在当前目录下
    #需要使用sys.path.append(./dynamic)使得目录指向当前目录下的dynamic目录
    sys.path.append(conf_info["dynamic_path"])
    frame = __import__(frame_name)#返回值标记这导入的模板
    app = getattr(frame, app_name)#此时app就指向了dymic下的mini_frame中的application函数
    wsgi_server = WSGIServer(port, app, conf_info["static_path"])
    wsgi_server.run_forever()
if __name__ == '__main__':
    main()