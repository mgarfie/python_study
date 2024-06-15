from pymysql import connect

conn = connect(
    host='localhost',
    port=3306,
    user='root',
    password='123456',
    autocommit=True         # 自动提交数据
)

# print(conn.get_server_info())

# 获取游标对象
cursor = conn.cursor()
# 选择数据库
conn.select_db("test")
# # 利用游标对象向数据传递SQL语言
# cursor.execute("create table test_pymysql(id int, name varchar(10), age varchar(5), sex varchar(5))")

# # 利用游标对象实现查询
# cursor.execute("select name from userdata")
# # 获取结果
# results: tuple = cursor.fetchall()                          # results是一个变量（返回值变量，类型为元组）
#
# for i in results:
#     print(i)
#


# 插入数据
cursor.execute("insert into userdata values(6, '毛玉琳', 19)")
conn.commit()                                 # 当有能改变数据的SQL语句时，需要用关键字commit来确认一下，要不不会生效


# 关闭数据库
conn.close()
