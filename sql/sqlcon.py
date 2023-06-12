import mysql.connector as msconn

def main():
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 's_school')
    mycur =  sqlcon.cursor()
    print()


def display():
    global mycur
    mycur.execute('select * from employee')
    mydata = mycur.fetchall()
    n_rec = mycur.rowcount
    print('the tot records are',n_rec)
    for row in mydata:
        print(row)

def search():
    pass

def insert():
    pass

def modify():
    pass

def delete():
    pass

if __name__ == '__main__':
    main()