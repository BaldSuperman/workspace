from pymysql import *
def main ():
    #创建connectiopn连接
    comn = connect(host='localhost',port=3306,user='root',password='123',database='jing_dong',charset='utf8')
    #huodecursor对象，得到游标对象cs1
    cursor = comn.cursor()
    #执行sql语句
    cursor.execute("""insert into goods_cates(name) values ("硬盘-new")""")
    #撤销当前的数据
    #comn.rollback()
    #最终提交数据请求
    comn.commit()

    #关闭游标
    cursor.close()
    #关闭连接
    comn.close()

if __name__ == '__main__':
    main()