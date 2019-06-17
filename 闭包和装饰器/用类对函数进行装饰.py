class Test(object):
    def __init__(self, func):
        self.func = func
    def __call__(self):
        print("这里是装饰器添加的共鞥")
        self.func()
@Test #相当于get_str = Test(get_str)
def get_str():
    return "hhhhhh"

print(get_str())