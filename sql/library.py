from datetime import date
import mysql.connector as msconn #pip install mysql-connector-python

def main():
    while True:
        print('='*40)
        print('\n\tLIBRARY MANAGEMENT\n')
        print('='*40,'\n\n\
        1. Books\n\
        2. Customer\n\
        3. Issue Book\n\
        4. Return Book\n\
        5. Exit\n')

        choice = int(input('Enter Choice: '))
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
        print('\nThe Total no of Books are',n_rec)
        for row in mydata:
            print(row[0],'|',row[1],'|',row[2],'|',row[3],'|',row[4],'|',row[5],'|',row[6],'|',row[7])
        print('\n')

    def search_book():
        cur_search = sqlcon.cursor()
        search = input('\nEnter Book Name or ISBN Number: ')

        if search.isnum():
            cur_search.execute('select * from books where ISBNo = "'+search+'"')
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
            cur.execute('update books set no_of_copies = %s where isbno = %s'%((int(data[0][0])+1),isbno))
        else:
            name = input('Enter Book Name: ')
            author = input('Enter Author: ')
            publisher = input('Enter Publisher: ')
            catagory = input('Enter Catogory: ')
            price = int(input('Enter Price: '))
            num = int(input('Enter Quantity: '))
            cur.execute('insert into books(isbno,book_name,author,publisher,catagory,price,no_of_copies) values(%s,"%s","%s","%s","%s",%s,%s)'%(isbno,name,author,publisher,catagory,price,num))

        sqlcon.commit()
        print('\n--Book Saved--\n')
        cur.close()

    def modify_book():
        cur_mod = sqlcon.cursor()
        custid = input('Enter ISBNo Of The Book Data You Want To Modify: \n')

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
            cur_mod.execute('update customers set Book_name = "%s" where CustID = "%s"'%(name,custid))
        elif choice == 2:
            auth = input('\nEnter Author: ')
            cur_mod.execute('update customers set Date_of_birth = "%s" where CustID = "%s"'%(dob,custid))
        elif choice == 3:
            pblshr = input('\nEnter Publisher: ')
            cur_mod.execute('update customers set address = "%s" where CustID = "%s"'%(address,custid))
        elif choice == 4:
            gnr = input('\nEnter Genre: ')
            cur_mod.execute('update customers set mobile = "%s" where CustID = "%s"'%(mob,custid))
        elif choice == 5:
            price = input('\nEnter Price: ')
            cur_mod.execute('update customers set Email = "%s" where CustID = "%s"'%(mail,custid))
        else :
            name = input('\nEnter Name to modify: ')
            dob = input('Enter Date Of Birth: ')
            address = input('Enter Address: ')
            mob = input('Enter Mobile Number: ')
            mail = input('Enter Email ID: ')

            cur_mod.execute('update customers set cust_name = "%s" where CustID = "%s"'%(name,custid))
            cur_mod.execute('update customers set Date_of_birth = "%s" where CustID = "%s"'%(dob,custid))
            cur_mod.execute('update customers set address = "%s" where CustID = "%s"'%(address,custid))
            cur_mod.execute('update customers set mobile = "%s" where CustID = "%s"'%(mob,custid))
            cur_mod.execute('update customers set Email = "%s" where CustID = "%s"'%(mail,custid))

        sqlcon.commit()
        print('--Customer Updated--')
        cur_mod.close()

    def delete_book():
        cur_del =  sqlcon.cursor()
        del_num = input('Enter ISBNo to delete: ')
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
        cur_disp.execute('select * from customer order by slno')
        mydata = cur_disp.fetchall()
        n_rec = cur_disp.rowcount
        print('\nThe Total no of customers are',n_rec)
        for row in mydata:
            print(row[0],'|',row[1],'|',row[2],'|',row[3],'|',row[4],'|',row[5],'|',row[6],'|',row[7])
        print('\n')

    def search_customer():
        cur_search = sqlcon.cursor()
        search = input('\nEnter |Customer Name or Customer ID Number: ')

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
        dob = input('Enter Date OF Birth: ')
        address = input('Enter Address: ')
        mob = int(input('Enter Mobile Number: '))
        mail = input('Enter Email ID: ')
        cur.execute('insert into books(CustID,Cust_name,age,date_of_birth,address,mobile,email) values(%s,"%s",%s,"%s","%s",%s,"%s")'%(custid,name,age,dob,address,mob,mail))

        sqlcon.commit()
        print('\n--ustomer Saved--\n')
        cur.close()

    def modify_customer():
        cur_mod = sqlcon.cursor()

        custid = input('Enter Customer ID Of The Customer Data You Want To Modify: \n')

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
            cur_mod.execute('update customers set cust_name = "%s" where CustID = "%s"'%(name,custid))
        elif choice == 2:
            dob = input('\nEnter Date Of Birth: ')
            cur_mod.execute('update customers set Date_of_birth = "%s" where CustID = "%s"'%(dob,custid))
        elif choice == 3:
            address = input('\nEnter Address: ')
            cur_mod.execute('update customers set address = "%s" where CustID = "%s"'%(address,custid))
        elif choice == 4:
            mob = input('\nEnter Mobile Number: ')
            cur_mod.execute('update customers set mobile = "%s" where CustID = "%s"'%(mob,custid))
        elif choice == 5:
            mail = input('\nEnter Email ID: ')
            cur_mod.execute('update customers set Email = "%s" where CustID = "%s"'%(mail,custid))
        else :
            name = input('\nEnter Name to modify: ')
            dob = input('Enter Date Of Birth: ')
            address = input('Enter Address: ')
            mob = input('Enter Mobile Number: ')
            mail = input('Enter Email ID: ')

            cur_mod.execute('update customers set cust_name = "%s" where CustID = "%s"'%(name,custid))
            cur_mod.execute('update customers set Date_of_birth = "%s" where CustID = "%s"'%(dob,custid))
            cur_mod.execute('update customers set address = "%s" where CustID = "%s"'%(address,custid))
            cur_mod.execute('update customers set mobile = "%s" where CustID = "%s"'%(mob,custid))
            cur_mod.execute('update customers set Email = "%s" where CustID = "%s"'%(mail,custid))

        sqlcon.commit()
        print('--Customer Updated--')

        cur_mod.close()

    def delete_customer():
        cur_del =  sqlcon.cursor()
        del_num = input('Enter CUST_ID to delete: ')
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
            add_customer()o
        elif choice == 4:
            modify_customer()
        elif choice == 5:
            delete_customer()
        else :
            break

#issuing
def issue_book():
    cur = sqlcon.cursor()
    isbno = int(input('\nEnter ISBNo of the book: '))
    cur.execute('select * from books where ISBNo = %s'%(isbno,))
    mydata = cur.fetchall()
    nbook = cur.rowcount

    if nbook != 0:
        custid = int(input('\nEnter Customer ID: '))
        tdate = str(date.today())
        cur.execute('select book_name from books where isbno = %s'%(isbno,))
        bookname = cur.fetchall()[0][0]
        cur.execute('select cust_name from customer where cust_id = %s'%(custid,))
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
    mydata = cur.fetchall()
    nbook = cur.rowcount

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
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'idris7', database = 'library')
    main()
    sqlcon.close()
