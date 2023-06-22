from datetime import date
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
            cur.execute('CREATE database library')
            sqldb.commit()
            cur.close()
            sqldb.close()
            sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')
            cur2 = sqlcon.cursor()
            cur2.execute('create table Books(slno int auto_increment UNIQUE, ISBNo int primary key, Book_Name varchar(50) not null, Author varchar(30) not null, Publisher varchar(30) not null, Genre varchar(30) not null, Price int not null, No_of_copies int)')
            cur2.execute('create table Customers(slno int auto_increment UNIQUE, CustID int primary key, Cust_Name varchar(50) not null, Age int(3) , Date_Of_Birth date,Address varchar(30) not null, Mobile bigint not null, Email varchar(50) not null)')
            cur2.execute('create table Issue(slno int auto_increment primary key, Date_of_issue DATETIME default now(),ISBno INT NOT NULL, Book_Name varchar(50) not null, Cust_ID int not null, Cust_Name varchar(30) not null,constraint mykey foreign key(ISBNo) references books(ISBNo),constraint mykey2 foreign key(Cust_ID) references customers(CustID))')
            cur2.execute('create table Returns(slno int auto_increment Primary key, Date_of_return DATETIME default now(),ISBno int NOT NULL, Cust_ID int not null,Fine_Amount decimal(10,2),paid char(1) ,constraint mykey3 foreign key(ISBNo) references books(ISBNo),constraint mykey4 foreign key(Cust_ID) references customers(CustID))')
            sqlcon.commit()
            cur2.close()
    else:
        cur.close()
        sqldb.close()
        sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')    

def main():
    while True:
        print('='*40)
        print('\n\tLIBRARY MANAGER\n')
        print('='*40,'\n\n\
        1. Books\n\
        2. Customer\n\
        3. Issue Book\n\
        4. Return Book\n\
        5. Exit\n')

        choice = int(input('Enter Choice: '))
        print('\n')
        if choice == 1:
            books()
        elif choice == 2:
            customer()
        elif choice == 3:
            issue_book()
        elif choice == 4:
            return_book()
        else :
            break

#books
def books():
    def disp_book():
        cur_disp =  sqlcon.cursor()
        cur_disp.execute('select * from books order by slno')
        mydata = cur_disp.fetchall()
        n_rec = cur_disp.rowcount
        if n_rec != 0:
            print('\nThe Total no of Books are',n_rec)
            for row in mydata:
                print(row[0],'|',row[1],'|',row[2],'|',row[3],'|',row[4],'|',row[5],'|',row[6],'|',row[7])
            print('\n')
        else:
            print('\n--No Books Found--\n')
        cur_disp.close()

    def search_book():
        cur_search = sqlcon.cursor()
        search = input('\nEnter Book Name or ISB Number: ')

        if search.isnumeric():
            cur_search.execute('select * from books where ISBNo = '+search)
        else:
            cur_search.execute('select * from books where Book_Name = "'+search+'"')

        data_search = cur_search.fetchall()
        print('\n')
        if data_search != None:
            for row in data_search:
                print(row)
            print('\n')
        else:
            print('\n--No Books found--\n')

        cur_search.close()

    def add_book():
        cur = sqlcon.cursor()

        isbno = int(input('\nEnter ISBNo: '))
        
        cur.execute('select no_of_copies from books where ISBNo = %s'%(isbno,))
        data = cur.fetchall()
        nbook = cur.rowcount

        if nbook != 0:
            num = int(input('Enter Quantity: '))
            cur.execute('update books set no_of_copies = %s where isbno = %s'%((int(data[0][0])+num),isbno))
        else:
            name = input('Enter Book Name: ')
            author = input('Enter Author: ')
            publisher = input('Enter Publisher: ')
            catagory = input('Enter Genre: ')
            price = int(input('Enter Price: '))
            num = int(input('Enter Quantity: '))
            cur.execute('insert into books(isbno,book_name,author,publisher,genre,price,no_of_copies) values(%s,"%s","%s","%s","%s",%s,%s)'%(isbno,name,author,publisher,catagory,price,num))

        sqlcon.commit()
        print('\n--Book Saved--\n')
        cur.close()

    def modify_book():
        cur_mod = sqlcon.cursor()
        isbno = input('\nEnter ISBNo Of The Book Data You Want To Modify: \n')

        print('\nEnter What You Want to modify\n\
        1. Book Name\n\
        2. Books Author\n\
        3. Books Publisher\n\
        4. Books Genre\n\
        5. Books Price\n\
        6. Modify All\n')

        choice = int(input('Enter Choice: '))
        if choice == 1:
            name = input('\nEnter Book Name: ')
            cur_mod.execute('update books set Book_name = "%s" where isbno = %s'%(name,isbno))
            print('\n--Name Updated--\n')
        elif choice == 2:
            auth = input('\nEnter Author: ')
            cur_mod.execute('update books set Author = "%s" where isbno = %s'%(auth,isbno))
            print('\n--Author Updated--\n')
        elif choice == 3:
            pblshr = input('\nEnter Publisher: ')
            cur_mod.execute('update books set Publisher = "%s" where isbno = %s'%(pblshr,isbno))
            print('\n--Publisher Updated--\n')
        elif choice == 4:
            gnr = input('\nEnter Genre: ')
            cur_mod.execute('update books set Genre = "%s" where isbno = %s'%(gnr,isbno))
            print('\n--Genre Updated--\n')
        elif choice == 5:
            price = input('\nEnter Price: ')
            cur_mod.execute('update books set Price = %s where isbno = %s'%(price,isbno))
            print('\n--Price Updated--\n')
        else :
            name = input('\nEnter Book Name: ')
            auth = input('\nEnter Author: ')
            pblshr = input('\nEnter Publisher: ')
            gnr = input('\nEnter Genre: ')
            price = input('\nEnter Price: ')

            cur_mod.execute('update books set Book_name = "%s",Author = "%s",Publisher = "%s",Genre = "%s",Price = %s where isbno = %s'%(name,auth,pblshr,gnr,price,isbno))
        
            print('--Book Updated--\n')

        sqlcon.commit()
        cur_mod.close()

    def delete_book():
        cur_del =  sqlcon.cursor()
        del_num = input('\nEnter ISBNo to delete: ')
        cur_del.execute('delete from books where isbno = '+str(del_num))
        print('\n--Book Deleted--\n')
        cur_del.commit()
        cur_del.close()

    while True:
        print('='*40)
        print('\n\tBook Manager\n')
        print('='*40,'\n\n\
        1. Display all Books\n\
        2. Search for a Book\n\
        3. Add a Book\n\
        4. Modify a Book\n\
        5. Delete a Book\n\
        6. Exit\n')

        choice = int(input('Enter Choice: '))
        if choice == 1:
            disp_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            add_book()
        elif choice == 4:
            modify_book()
        elif choice == 5:
            delete_book()
        else :
            break

#customers
def customer():
    def disp_customer():
        cur_disp =  sqlcon.cursor()
        cur_disp.execute('select * from customers order by slno')
        mydata = cur_disp.fetchall()
        n_rec = cur_disp.rowcount
        if n_rec != 0:
            print('\nThe Total no of customers are',n_rec)
            for row in mydata:
                print(row[0],'|',row[1],'|',row[2],'|',row[3],'|',row[4],'|',row[5],'|',row[6],'|',row[7])
            print('\n')
        else:
            print('\n--No Customerss Found--\n')
        cur_disp.close()

    def search_customer():
        cur_search = sqlcon.cursor()
        search = input('\nEnter Customer Name or Customer ID Number: ')

        if search.isnum():
            cur_search.execute('select * from Customer where ISBNo = "'+search+'"')
        else:
            cur_search.execute('select * from Customer where Book_Name = "'+search+'"')

        data_search = cur_search.fetchall()
        print('\n')
        if data_search != None:
            for row in data_search:
                print(row)
            print('\n')
        else:
            print('\n--No Customer found--\n')

        cur_search.close()

    def add_customer():
        cur = sqlcon.cursor()

        custid = int(input('\nEnter Customer ID: '))
        name = input('Enter Customer Name: ')
        age = int(input('Enter Age: '))
        dob = input('Enter Date of Birth (yyyy-mm-dd): ')
        address = input('Enter Address: ')
        mob = int(input('Enter Mobile Number: '))
        mail = input('Enter Email ID: ')
        cur.execute('insert into customers(CustID,Cust_name,age,date_of_birth,address,mobile,email) values(%s,"%s",%s,"%s","%s",%s,"%s")'%(custid,name,age,dob,address,mob,mail))

        sqlcon.commit()
        print('\n--Customer Saved--\n')
        cur.close()

    def modify_customer():
        cur_mod = sqlcon.cursor()

        custid = input('\nEnter Customer ID Of The Customer Data You Want To Modify: \n')

        print('\nEnter What You Want to modify\n\
        1. Customer Name\n\
        2. Customers Date Of Birth\n\
        3. Customers Address\n\
        4. Customers Mobile Number\n\
        5. Customers Email ID\n\
        6. Modify All\n')

        choice = int(input('Enter Choice: '))
        if choice == 1:
            name = input('\nEnter Customer Name: ')
            cur_mod.execute('update customers set cust_name = "%s" where CustID = %s'%(name,custid))
        elif choice == 2:
            dob = input('\nEnter Date Of Birth: ')
            cur_mod.execute('update customers set Date_of_birth = "%s" where CustID = %s'%(dob,custid))
        elif choice == 3:
            address = input('\nEnter Address: ')
            cur_mod.execute('update customers set address = "%s" where CustID = %s'%(address,custid))
        elif choice == 4:
            mob = int(input('\nEnter Mobile Number: '))
            cur_mod.execute('update customers set mobile = %s where CustID = %s'%(mob,custid))
        elif choice == 5:
            mail = input('\nEnter Email ID: ')
            cur_mod.execute('update customers set Email = "%s" where CustID = %s'%(mail,custid))
        else :
            name = input('\nEnter Name to modify: ')
            dob = input('Enter Date Of Birth: ')
            address = input('Enter Address: ')
            mob = int(input('Enter Mobile Number: '))
            mail = input('Enter Email ID: ')

            cur_mod.execute('update customers set cust_name = "%s",Date_of_birth = "%s",address = "%s",mobile = "%s",Email = "%s" where CustID = "%s"'%(name,dob,address,mob,mail,custid))

        sqlcon.commit()
        print('\n--Customer Updated--\n\n')

        cur_mod.close()

    def delete_customer():
        cur_del =  sqlcon.cursor()
        del_num = input('\nEnter Customer ID to delete: ')
        cur_del.execute('delete from customers where custid = '+str(del_num))
        print('\n--Customer Deleted--\n')
        cur_del.commit()
        cur_del.close()

    while True:
        print('='*40)
        print('\n\tCustomer Manager\n')
        print('='*40,'\n\n\
        1. Display all Customer\n\
        2. Search for a Customer\n\
        3. Add a Customer\n\
        4. Modify a Customer\n\
        5. Delete a Customer\n\
        6. Exit\n')

        choice = int(input('Enter Choice: '))
        if choice == 1:
            disp_customer()
        elif choice == 2:
            search_customer()
        elif choice == 3:
            add_customer()
        elif choice == 4:
            modify_customer()
        elif choice == 5:
            delete_customer()
        else :
            break

#issuing
def issue_book():
    cur = sqlcon.cursor()
    isbno = int(input('Enter ISBNo of the book: '))
    cur.execute('select * from books where ISBNo = %s'%(isbno,))
    nbook = cur.fetchall()[0][7]

    if nbook != 0:
        custid = int(input('\nEnter Customer ID: '))
        tdate = str(date.today())
        cur.execute('select book_name from books where isbno = %s'%(isbno,))
        bookname = cur.fetchall()[0][0]
        cur.execute('select cust_name from customers where custid = %s'%(custid,))
        custname = cur.fetchall()[0][0]

        cur.execute('update books set no_of_copies = "%s" where isbno = "%s"'%(nbook-1,isbno))
        cur.execute('insert into issue(date_of_issue,isbno,book_name,cust_id,cust_name) values("%s",%s,"%s",%s,"%s")'%(tdate,isbno,bookname,custid,custname))
        sqlcon.commit()
        print('\n--Book Issued--\n')
    else:
        print('\n--Book Out of Stock--\n')

    cur.close()

#returning
def return_book():
    cur = sqlcon.cursor()
    isbno = int(input('\nEnter ISBNo of the book: '))
    cur.execute('select * from books where ISBNo = %s'%(isbno,))
    nbook = cur.fetchall()[0][7]

    if nbook != 0:
        custid = int(input('\nEnter Customer ID: '))
        tdate = str(date.today())
        cur.execute('select book_name from books where isbno = %s'%(isbno,))
        bookname = cur.fetchall()[0][0]
        cur.execute('select cust_name from customer where cust_id = %s'%(custid,))
        custname = cur.fetchall()[0][0]

        cur.execute('update books set no_of_copies = "%s" where isbno = "%s"'%(nbook+1,isbno))
        cur.execute('insert into return(date_of_issue,isbno,book_name,cust_id,cust_name) values("%s",%s,"%s",%s,"%s")'%(tdate,isbno,bookname,custid,custname))
        sqlcon.commit()
        print('\n--Book Returned--\n')
    else:
        print('\n--Book Out of Stock--\n')

    cur.close()

if __name__ == '__main__':
    sqldb = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy')
    check_database()
    main()
    sqlcon.close()