def set_func(func):
    #需要给函数call_func传递参数
    def call_func(*args, **kwargs):
        print("hahhahah")
        #func(args, kwargs)相当于传递了一个元组，一个字典
        return func(*args, **kwargs)#拆包
    return call_func
@set_func#等价于test1 = set_func(test1)
def test1(num, *args, **kwargs):
    print("-------test1--------%d"%num)
    print("-------test1--------", args)
    print("-------test1--------", kwargs)
    return "ok"
@set_func
def test2(num, *args, **kwargs):
    pass
ret = test1(100)
print(ret)
ret = test2(100)
print(ret)