import re

def main():
    names = ["age", "_age1", "YUYIHH", "tJJJ_OOO", "DADADA!!!", "1age", "%ages", "_____"]
    for name in names:
        #ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*", name)
        #末尾加上$表示必须匹配到结尾,^表示必须匹配字符串开头
        ret = re.match(r"[a-zA-Z_][a-zA-Z0-9_]*$", name)
        if ret :
           # print("变量名{0}符合要求,通过正则匹配出来的记过".format(ret.group()))
            print("变量名{0}符合要求,通过正则匹配出来的记过".format(name))
        else :
            print("变量名{0}不符合要求".format(name))
if __name__ == '__main__':
    main()