from urllib import request
'''
使用urllib.requests请求一个网页内容，并把内容打印出来
'''
if __name__ == '__main__':
    url = "https://www.qidian.com/"
    #打开url并把相应页面作为返回
    rsp = request.urlopen(url)
    #把返回的结果读取出来
    #读取出来的内容类型为bytes
    html = rsp.read()
    print(type(html))
    # 如果想把内容转换为字符串，需要解码
    html = html.decode()
    print(html)
