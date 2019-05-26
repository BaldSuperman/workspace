'''
a利用request下载页面
自动检测页面编码

'''
from urllib import request,parse
import chardet
if __name__ == '__main__':
    url = "https://www.baidu.com/s?"
    wd = input("请输入查询内容： ")
    #要想使用data，需要使用字典
    qs = {
        "wd": wd

    }
    #给qs编码
    qs = parse.urlencode(qs)
    fullurl = url + qs
    print(fullurl)
    rsp = request.urlopen(fullurl)

    html = rsp.read()

    html = html.decode()
   # print(html)
    print(html)