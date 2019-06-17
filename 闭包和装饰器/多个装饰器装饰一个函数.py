def add_qx(func):
    #需要给函数call_func传递参数
    def call_func(*args, **kwargs):
        print("hahhahah")
        #func(args, kwargs)相当于传递了一个元组，一个字典
        print("这是装饰1权限的功能一")
        func(*args, **kwargs)#拆包
    return call_func
def add_xx(func):
    #需要给函数call_func传递参数
    def call_func(*args, **kwargs):
        print("hahhahah")
        #func(args, kwargs)相当于传递了一个元组，一个字典
        print("这是装饰2权限的功能一")
        func(*args, **kwargs)#拆包
    return call_func
@add_qx
@add_xx
def test1():
    print("-----test1--------=-")

test1()

