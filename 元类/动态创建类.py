class Test1:
    num = 100
    num2 = 200

#动态创建
Test2 = type("Test2",(),{"num":100, "num2": 200})
help(Test1)
help(Test2)