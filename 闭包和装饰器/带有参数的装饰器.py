def set_func(func):
    def call_func(*args, **kwargs):
        leve1 = args[0]
        if leve1 == 1:
            print('----权限级别1"')
        elif leve1 == 2:
            print('----权限级别2"')
        return func()
    return  call_func

@set_func
def test1():
    print("----test----")
    return "ok"
@set_func
def test2():
    print("-----test2----")
    return "ok"
test1()