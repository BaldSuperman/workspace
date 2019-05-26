import re
'''
. :匹配单个字符,除了\n
[]:匹配[]中的一个元素
\d:匹配数字0-9
\D:匹配非数字
\s:匹配空白
\S：匹配非空白
\w:匹配单词字符，即a-z,A-Z，0-9，_
\W：匹配非单词字符
'''
#查看需要查询的内容中是否有速度与激情+一个数字
ret = re.match(r"速度与激情\d", "速度与激情3")
print(ret)
print(ret.group())
#查看需要查询的内容中是否有速度与激情+1~8数字母
ret = re.match(r"速度与激情[12345678]", "速度与激情3阿斯顿啊的")
print(ret)
print(ret.group())
#查看需要查询的内容中是否有速度与激情+1-8（简洁的写法）
ret = re.match(r"速度与激情[1-8]", "速度与激情3阿斯顿啊的")
print(ret)
print(ret.group())
#查看需要查询的内容中是否有速度与激情+123478（简洁的写法）
ret = re.match(r"速度与激情[1-47-8]", "速度与激情7")
print(ret)
print(ret.group())
#查看需要查询的内容中是否有速度与激情+123478+abcd（简洁的写法）
ret = re.match(r"速度与激情[1-47-8a-d]", "速度与激情b")
print(ret)
print(ret.group())