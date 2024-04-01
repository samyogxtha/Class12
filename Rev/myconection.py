import mysql.connector as mscon

conn = mscon.connect(user='root',host='localhost',passwd='samy',database='test')

cur = conn.cursor()

cur.execute('select * from employee')

print(cur.fetchone())
print(cur.fetchmany(2))
l = cur.fetchall()

print(l,type(l))