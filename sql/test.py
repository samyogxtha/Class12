import mysql.connector as msconn
from tabulate import tabulate
sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')


cur_disp =  sqlcon.cursor()
cur_disp.execute('select * from books order by slno')
data = cur_disp.fetchall()
n_rec = cur_disp.rowcount
if n_rec != 0:
    print(tabulate(data, headers=['slno','ISBNo','Book Name','Author','Publisher','Genre','Price','Quantity'], tablefmt="rounded_outline"))
else:
    print('\n--No Books Found--\n')
cur_disp.close()