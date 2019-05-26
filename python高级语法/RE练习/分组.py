import re
'''
| :匹配左右任意一个表达式
（ab）:将括号中字符作为一个分组
\num :引用num匹配到的字符串
（？P<NAME>）:分组起别名
(?P=name):引用别名为name分组匹配到的字符串
'''
rtc = re.match(r"([A-Za-z0-9]*)@(163|126)\.com","yang@126.com")
print(rtc.group(1))
print(rtc.group(2))
html_str = "<h1>hhhhhhhahdhadha</h1>"
rtc = re.match("<\w*>.*</\w*>", html_str)
print(rtc)
rtc = re.match("<(\w*)>.*</\1>", html_str)
print(rtc)