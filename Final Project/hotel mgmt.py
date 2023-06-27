import datetime as dt
from tabulate import tabulate
import mysql.connector as msconn #pip install mysql-connector-python

#chk database
def check_database():
    global sqlcon
    cur = sqldb.cursor()
    cur.execute('show databases')
    db = cur.fetchall()
    dbs = []
    for i in db:
        dbs.append(i[0])
    if 'library' not in dbs:
            cur.execute('CREATE database hotel')
            sqldb.commit()
            cur.close()
            sqldb.close()
            sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = '%s'%(passw,), database = 'hotel')
            cur2 = sqlcon.cursor()
            cur2.execute('create table Books(slno int auto_increment UNIQUE, ISBNo int primary key, Book_Name varchar(50) not null, Author varchar(30) not null, Publisher varchar(30) not null, Genre varchar(30) not null, Price int not null, No_of_copies int)')
            cur2.execute('create table Customers(slno int auto_increment UNIQUE, Cust_ID int primary key, Cust_Name varchar(50) not null, Age int(3) , Date_Of_Birth date,Address varchar(30) not null, Mobile bigint not null, Email varchar(50) not null)')
            cur2.execute('create table Issue(slno int auto_increment primary key, Date_of_issue DATETIME default now(),ISBno INT NOT NULL, Book_Name varchar(50) not null, Cust_ID int not null, Cust_Name varchar(30) not null,constraint mykey foreign key(ISBNo) references books(ISBNo),constraint mykey2 foreign key(Cust_ID) references customers(Cust_ID))')
            cur2.execute('create table Returns(slno int auto_increment Primary key, Date_of_return DATETIME default now(),ISBno int NOT NULL, Cust_ID int not null,Fine_Amount decimal(10,2),paid char(1) ,constraint mykey3 foreign key(ISBNo) references books(ISBNo),constraint mykey4 foreign key(Cust_ID) references customers(cust_id))')
            sqlcon.commit()
            cur2.close()
    else:
        cur.close()
        sqldb.close()
        sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')    

def main():
    while True:
        print('\n')
        print('='*40,'\n\n\tLIBRARY MANAGER\n')
        print('='*40,'\n\
        1. Books\n\
        2. Customer\n\
        3. Issue Book\n\
        4. Return Book\n\
        5. View Issues\n\
        6. View Returns\n\
        7. Exit\n')

        choice = int(input('Enter Choice: '))
        print('\n')
        '''if choice == 1:
            books()
        elif choice == 2:
            customer()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            view_issues()
        elif choice == 6:
            view_returns()
        else :
            print('\t--Thank You.!--\n')
            break
'''

if __name__ == '__main__':
    global passw
    passw = input('Enter Password: ')
    sqldb = msconn.connect(host = 'localhost', user = 'root', passwd = '%s'%(passw,))
    check_database()
    main()
    sqlcon.close()