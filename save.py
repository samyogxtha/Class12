import mysql.connector as msconn #pip install mysql-connector-python

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'school')

cur = sqlcon.cursor()
cur.execute('select name from employee where empno = 101')
bookname = cur.fetchall()[0]
cur.execute('select dept from employee where empno = 7')
custname = cur.fetchall()[0][0]

print(bookname,custname)
cur.close()