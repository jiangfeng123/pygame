"""
#1导入模块
#2建立连接对象  pymysql.connect()
#3建立游标对象
#4使用游标对象执行sql
#5获取执行的结果
#6打印输出内容
#7关闭游标对象
#8关闭连接对象

"""
#1导入模块
import pymysql
#2建立连接对象  pymysql.connect()
                #参数host 主机
                #user  用户名
                #password  密码
                #database   指定数据库

conn = pymysql.connect(host="localhost",user="root",password="123456",database="python_test_1")
#3建立游标对象
cur = conn.cursor()
#4使用游标对象执行sql


#被注入的过程的分析
#sql = "select * from students where name = '%s' order by id desc" % input_name
#select * from students where name = '' or 1 or '' order by id desc

#防止注入：
#      
#1)构建参数列表params = input_name
#2)把列表传递给execute

            #cur.execute(sql语句) ,返回值是影响的行数，如果是查询语句，此处返回总记录数
input_name = input("请输入要查询的名称：")
params = [input_name]
sql = "select * from students where name = %s order by id desc"


result = cur.execute(sql,params)
print("查询到%s条数据" % result)
#5获取执行的结果
#result_list = cur.fetchone()#fetchone  从查询的结果取出一条数据   
result_list = cur.fetchall()
#6打印输出内容
for line in result_list:
    print(line)
#7关闭游标对象
cur.close()
#8关闭连接对象
conn.close()
