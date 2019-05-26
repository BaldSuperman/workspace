'''
a利用request下载页面
自动检测页面编码

'''
from urllib import request
import chardet
if __name__ == '__main__':
    url = "https://www.cnblogs.com/lijc1990/p/3480710.html"
    rsp = request.urlopen(url)
    print(rsp)
    print(type(rsp))
    print("URL:{0}".format(rsp.geturl() ))
    print("INFO:{0}".format(rsp.info()))
    print("Code:{0}".format(rsp.getcode()))
    html = rsp.read()

    html = html.decode()
   # print(html)