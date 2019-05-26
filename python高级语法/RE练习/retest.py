"""
RE使用步骤
1 使用compilc将表示正则的字符串编译为一个pattern对象
2 通过pattern对象提供的一系列方法对文本进行匹配查找获得匹配结果，一个Match对象
3 最后使用Match对象提供的属性和方法获得信息，根据需要操作
Re常用函数
- group():获得一个或多个分组匹配的字符串，当获得整个匹配的子串时，直接使用gourp或者froup（0）
- start：获取分组匹配的子串在整个字符串中的其实位置，默认参数为0
-end ：获取分组匹配的子串在整个字符串中的结束位置，默认为0
- soan： 返回的结构技术（start(gourp),end(group)
"""
#导入相关包
import re


#查找数字
#r表示字符串不转义
p = re.compile(r'\d+')
#在字符串中进行查找，按照规则p指定的正则进行查找
# 参数1，9表示在字符串中查找的范围
m = p.match("one1234333kksada34", 3, 17)
# 返回结果时None表示没找到，否则返回match对象
print(m)
# 代码说明问题
# 可以输入参数表示起的位置
#查找到的结果只包含一个，表示第一次进行匹配成功的内容

#re.I表示忽略大小写 寻找2组最少有一个字母的分组
p1 = re.compile(r'([a-z]+) ([a-z]+)', re.I)
m = p1.match("wo shi yang xiugui")
print(m.group(1))
print(m)

#查找 search（str,[,pos[,endpos]]）在字符串中查找匹配，pos和endpos表示起始位置
# findall:查找所有
#finditer 查找，返回一个iter结果

p = re.compile(r'\d+')
m =p.search("one123wda13232asd11332")
print(m.group())
rst = p.findall("one123wda13232asd11332")
print(rst)

# sub替换
#- sub(rep1, str[,count])

p = re.compile(r'(\w+) (\w+)')
s = "hello 123 wang 456 xiaojing, i love you"
rst = p.sub(r'Hellow word', s)
print(rst)

# 匹配中文
# - 大部分中文内容表示范围是[u4c00-u9fa5],不包括全角标点
title = u'世界，你好， hellow moto'
p = re.compile(r'[\u4c00-\u9fa5]+')
rst = p.findall(title)
print(rst)
# -贪婪和非贪婪
    #-贪婪：尽可能多的匹配，.（*）表示贪婪匹配
    #-非贪婪：找到符合条件的最小内容即可，（？）表示非贪婪
    #-正则默认使用贪婪匹配
title = u'<div>name</div><div>age</div>'
p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")
m1 = p1.search(title)
print(m1.group())
m2 = p2.search(title)
print(m2.group())