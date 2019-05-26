import re
'''
* :匹配前一个字符出现0次或者无限次即可有可无
+ ：匹配前一个字符出现1次或者无限次，即至少有一次
？ ：匹配其哪一个字符出现1次或0次
{m}:匹配前一个字符出现m次
{m ,n}:匹配前一个字符出现m-n次

'''

#判读数据中有没有速度与激情+1~3个数字
print(re.match(r"速度与激情\d{1,3}", "速度与激情12"))
#判读数据中有没有速度与激情+11,只能有11位
print(re.match(r"速度与激情\d{11}", "速度与激情12121212121"))
#？前面的一位数据可以有可以没有
print(re.match(r"\w?速度与激情\d{1,3}", "速度与激情12"))
#*前面的一位数据可以有可以有无限个也可以没有,re.S:让.包含\n
print(re.match(r"2*速度与激情\d{1,3}", "2222速度与激情12"))
print(re.match(r".*速度与激情\d{1,3}", "dad a ssa速度与激情12"))
html_data = "dadada \nd aa d asd asd asd\nda da d ad asd a"
print(re.match(r".*", html_data, re.S))
