def set_func(func):
    def call_func():
        print("hahhahah")
        func()
    return call_func
@set_func#等价于test1 = set_func(test1)
def test1():
    print("-------test1--------")
test1 = set_func(test1)
test1()