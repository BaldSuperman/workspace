def set_func(func):
    #需要给函数call_func传递参数
    def call_func(num):
        print("hahhahah")
        func(num)
    return call_func
@set_func#等价于test1 = set_func(test1)
def test1(num):
    print("-------test1--------%d"%num)

test1(100)