'''
a利用request下载页面
自动检测页面编码

'''
from urllib import request
import chardet
if __name__ == '__main__':
    url = "https://www.cnblogs.com/lijc1990/p/3480710.html"
    rsp = request.urlopen(url)
    html = rsp.read()
    # 利用chardet自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)
    # 利用get取值保证不会出错
    html = html.decode(cs.get("encoding", "utf-8"))
    print(html)