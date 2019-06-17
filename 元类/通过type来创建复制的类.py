class Test1:
    num = 100
    num2 = 200

class Test11(Test1):
    pass
#动态创建以及继承
Test2 = type("Test2",(),{"num":100, "num2": 200})
Test22 = type("Test2",(Test2,),{})
#添加实例方法

def test_2(self):
    print("实例方法")
Test3 = type("Test3",(),{"test_2":test_2})
help(Test3)
t3 = Test3()
t3.test_2()

#添加类方法
@classmethod
def test_3(cls):
    print("这是类方法")
Test4 = type("Test4",(),{"test_2":test_2,"test_3":test_3})
help(Test4)
Test4.test_3()
#添加静态方法
@staticmethod
def test_4():
    print("这是静态方法")
Test5 = type("Test5",(),{"test_2":test_2,"test_3":test_3,"test_4":test_4})

help(Test5)
Test5.test_4()