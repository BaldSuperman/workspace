'''
利用parse模块模拟post请求
和案例5一样，只是使用requests来实现
分析百度词典
分析步骤
1 打开F12
2 尝试输入单词girl，发现每一个字母后面都有请求
3 请求地址是https://fanyi.baidu.com/sug
4 利用network-all-hearders查看，发现FormDate的值是kw：girl
5 检查返回格式，发现是json格式的内容，需要用到json包
'''
from urllib import request, parse
import json

'''
大致流程是：
1 利用data构造内容，然后urlopen打开
2 返回一个json'格式的结果
3 结果应该是girl的释义
'''
baseurll = "https://fanyi.baidu.com/sug"

kw = input("请输入查询的单词")
#字典格式
data = {
    'kw' : kw
}
#使用parse模块对date进行编码
data = parse.urlencode(data)#str类型，准换为二进制
data = data.encode()
#我们需要构造一个请求头，请求头都应该至少包含传入的数据的长度
#request要求传入的请求头是要给dict格式
headers = {
    #因为使用post，至少应该包含content-lenth 字段
    'Content-Lenth':len(data)
}
#有个headers。data。url，就可以尝试发出请求了
req = request.Request(url=baseurll, data=data, headers=headers)
#因为已经构造了一个Request实例，所有的请求信息可以封装到Requests实例中
rsp = request.urlopen(req)
json_data = rsp.read().decode()
print(json_data)
#把json字符串转换为字典
json_data = json.loads(json_data)
print(json_data)
for item in json_data['data']:
    print(item["k"], "--", item['v'])