def line_6(k, b):
    def create_y(x):
        print(k*x+b)
    return create_y()

line6_1 = line_6(1, 2) #得到时create_y函数并且该函数有变量1，2
line6_1(0)
