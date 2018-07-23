#导入MySQL驱动
import mysql.connector
#注意把password设为自己的口令
conn = mysql.connector.connect(user = 'qwang', password = 'wq131104037',database = 'test')
cursor = conn.cursor()
#创建user表
cursor.execute('create table user2 (id varchar(20) primary key, name varchar(20))')
#插入一行记录，注意MySQL的占位符是%s
cursor.execute('insert into user2 (id,name) values (%s,%s)',['1','Michael'])
print(cursor.rowcount)
#提交事务
conn.commit()
cursor.close()
#运行查询
cursor = conn.cursor()
cursor.execute('select * from user2 where id = %s',('1',))
values = cursor.fetchall()
print(values)
cursor.close()
conn.close() 