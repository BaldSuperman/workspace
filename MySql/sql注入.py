from pymysql import *
class JD(object):
    def __init__(self):
        # 创建connectiopn连接
        self.comn = connect(host='localhost', port=3306, user='root', password='123', database='jing_dong', charset='utf8')
        # huodecursor对象，得到游标对象cs1
        self.cursor = self.comn.cursor()
    def __del__(self):
        self.cursor.close()
        self.comn.close()
    #查询的命令运行的记过
    def execute_sql(self, sql):
        self.cursor.execute(sql)
        for temp in self.cursor.fetchall():
            print(temp)
    def show_all_items(self):
        #显示所有商品
        sql = "select * from goods;"
        self.execute_sql(sql)

    def show_cates(self):
        sql = "select name from goods_cates;"
        self.execute_sql(sql)

    def show_brands(self):
        sql = "select name from goods_brands;"
        self.execute_sql(sql)
    def add_bradns(self):
        item_name = input("输入新商品名称: ")
        sql ="""insert into goods_cates(name) values ("%s")"""% item_name
        self.cursor.execute(sql)
        self.comn.commit()
    def get_info_by_name(self):
        #防止sql注入
        find_name = input("请输入要查询的商品名字： ")
        sql = "select * from goods where name=%s"
        #防止sql注入使用列表直接填充
        self.cursor.execute(sql, [find_name])
        print(self.cursor.fetchall)
    #定义为静态方法
    @staticmethod
    def print_menu():
        print("------京东-------")
        print("1:所有的商品")
        print("2:所有的商品分类")
        print("3 所有的商品品牌分类")
        print("4 添加一个商品分类")
        print("5 根据名字查询商品")
        return input("请输入功能对应的序号： ")

    def run(self):
        while True:
            num = self.print_menu()
            if num == "1":
                #查询商品
                self.show_all_items()

            elif num == "2":
                #查询分类
                self.show_cates()
            elif num =="3":
                #查询品牌分类
                self.show_brands()
            elif num == "4":
                # 添加商品分类
                self.add_bradns()
            elif num == "5":
                # 根据名字查询商品
                self.get_info_by_name()

            else:
                print("命令有误")

def main():
    #1 创建一个京东商城对象
    jd = JD()
    #2 调用这个对象的run方法，让其运行
    jd.run()

if __name__ == '__main__':
    main()