import re

def main():
    email = input("请输入一个邮箱地址")
    ret = re.match(r"[a-zA-Z0-9]{4,20}@163\.com$", email)#\反斜杠表示转义
    if ret:
        print("keyi")
    else:
        print("bukeyi")

if __name__=="__main__":
    main()