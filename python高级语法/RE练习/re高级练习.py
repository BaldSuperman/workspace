'''
python中独有的功能
search：不需要从头匹配数据，只需要在全部中查找符合条件的
findall : 返回值是符合条件的一个列表
sub: 将正则匹配到的值换成自己定的值re.sub(正则表达式，替换的值，原数据）
sub(正则表达式，函数名，数据）把数据中符合条件的返回值用到函数中，得到函数调用后的结果
solit:切割re.split(r":\"，数据）将数据中的;或者空格 分割
'''
import re
rst = re.search(r"\d+", "阅读次数：9999 点赞数： 9090")
print(rst.group())
#使用findall不需要使用group
rst = re.findall(r"\d+", "阅读次数：9999 点赞数： 9090")
print(rst)
#替换
rst = re.sub(r"\d+", "333",  "阅读次数：9999 点赞数： 9090")
print(rst)
#分割
rst = re.split(r":| ", "yanga fda:woshioge alkjsdlkajs:dad")
print(rst)