
'''
create table goods(
    id int unsigned primary key auto_increment not null,
    name varchar(150) not null,
    cate_name varchar(40) not null,
    brand_name varchar(40) not null,
    price decimal(10,3) not null default 0,
    is_show bit not null default 1,
    is_salceff bit not null default 0
);
create table info(
    id int unsigned primary key auto_increment not null,
    code int ,
    short varchar(40) not null,
    chg varchar(40) not null,
    time date
);
insert into goods values(0,0007,"quanxinhao”,"10",2017-01-03）;
insert into info values(1,00025,"quadas","20",20170103);
insert into info values(0,00507,"qadadasdnxinhao","10",20170103);
insert into info values(0,00037,"quanxadahao","11",2017110103);
insert into info values(0,00022,"quandaaao","122",201720103);
insert into goods values(0,"huawei m5","bijiben","huawei",'3393',default,default);
insert into goods values(0,"huawei m6","bijiben","huawei",'33943',default,default);
insert into goods values(0,"huawei m7","bijiben","huawei",'33933',default,default);
insert into goods values(0,"huawei m8","bijiben","huawei",'33923',default,default);
insert into goods values(0,"huawei m9","bijiben","huawei",'33934',default,default);
insert into goods values(0,"xiaomi m2","bijiben","xiaomi",'32343',default,default);

insert into goods values(0,"huawei m5","cjbijiben","huawei",'3393',default,default);
insert into goods values(0,"huawei m6","bcjbijiben","huawei",'33943',default,default);
insert into goods values(0,"huawei m7","jybijiben","huawei",'33933',default,default);
insert into goods values(0,"huawei m8","cjbijiben","huawei",'33923',default,default);
insert into goods values(0,"huawei m9","ccbijiben","huawei",'33934',default,default);
insert into goods values(0,"xiaomi m2","ssbijiben","xiaomi",'32343',default,default);

select *
from (select cate_name,max(price) as max_price from goods group by cate_name) as g_new
left join goods as g
on g_new.cate_name=g.cate_name and g_new.max_price=g.price;
'''
from pymysql import *
def main ():
    #创建connectiopn连接
    comn = connect(host='localhost',port=3306,user='root',password='123',database='jing_dong',charset='utf8')
    #huodecursor对象，得到游标对象cs1
    cursor = comn.cursor()
    #执行sql语句
    cursor.execute("select* from goods;")
    #得到游标得到的结果 得到一个结果
    print(cursor.fetchone())
    #得到多个结果
    print(cursor.fetchmany(3))
    #得到所有结果
    print(cursor.fetchall())
    #关闭游标
    cursor.close()
    #关闭连接
    comn.close()

if __name__ == '__main__':
    main()




















