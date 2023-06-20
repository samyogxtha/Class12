from datetime import date
import mysql.connector as msconn #pip install mysql-connector-python

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')

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
            print(row[0],'|',row[1],'|',row[2],'|',row[3])
        print('\n')

    def search_book():
        cur_search = sqlcon.cursor()
        search = input('\nEnter Book Name or ISBN Number: ')

        if search.isalnum():
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

    def insert_book():
        cur_insert = sqlcon.cursor()

        isbno = int(input('\nEnter ISBNo: '))
        name = input('Enter Book Name: ')
        author = input('Enter Author: ')
        publisher = input('Enter Publisher: ')
        catagory = input('Enter Catogory: ')
        price = int(input('Enter Price: '))
        num = int(input('Enter Quantity: '))

        cur_insert.execute('insert into books(isbno,book_name,author,publisher,catagory,price,no_of_copies) values(%s,"%s","%s","%s","%s",%s,%s)'%(isbno,name,author,publisher,catagory,price,num))
        sqlcon.commit()
        print('\n--Book Saved--\n')
        cur_insert.close()

    def modify_book():
        cur_mod = sqlcon.cursor()

        isbno = int(input('\nEnter ISBNo to modify: '))
        price = int(input('Enter Salary: '))
        
        cur_mod.execute('update books set price = "%s" where isbno = "%s"'%(price,isbno))
        sqlcon.commit()
        print('Price Updated')

        cur_mod.close()

    def delete_book():
        cur_del =  sqlcon.cursor()
        del_num = input('Enter ISBNo to delete: ')
        cur_del.execute('delete from books where isbno = '+str(del_num))
        print('\nBook Deleted.\n')
        cur_del.close()

    while True:
        print('='*40)
        print('\n\tBook Manager\n')
        print('='*40,'\n\n\
        1. Display all Books\n\
        2. Search for a Book\n\
        3. Insert an Book\n\
        4. Modify an Book\n\
        5. Delete an Book\n\
        6. Exit\n')
        
        choice = int(input('Enter Choice: '))
        if choice == 1:
            disp_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            insert_book()
        elif choice == 4:
            modify_book()
        elif choice == 5:
            delete_book()
        else :
            break

#customers
def customer():
    def disp_book():
        cur_disp =  sqlcon.cursor()
        cur_disp.execute('select * from books order by slno')
        mydata = cur_disp.fetchall()
        n_rec = cur_disp.rowcount
        print('\nThe Total no of Books are',n_rec)
        for row in mydata:
            print(row[0],'|',row[1],'|',row[2],'|',row[3])
        print('\n')

    def search_book():
       pass

    def insert_book():
        pass

    def modify_book():
        pass

    def delete_book():
        pass

    while True:
        print('='*40)
        print('\n\tBook Manager\n')
        print('='*40,'\n\n\
        1. Display all Books\n\
        2. Search for a Book\n\
        3. Insert an Book\n\
        4. Modify an Book\n\
        5. Delete an Book\n\
        6. Exit\n')
        
        choice = int(input('Enter Choice: '))
        if choice == 1:
            disp_book()
        elif choice == 2:
            search_book()
        elif choice == 3:
            insert_book()
        elif choice == 4:
            modify_book()
        elif choice == 5:
            delete_book()
        else :
            break

#issuing
def issue_book():
    cur = sqlcon.cursor()
    isbno = int(input('\nEnter ISBNo of the book: '))
    cur.execute('select * from books where ISBNo = %s'%(isbno,))
    data_search = cur.fetchall()
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
        print('Book Issued')
    else:
        print('\n--Book Out of Stock--\n') 

    cur.close()

#returning
def return_book():
    cur_mod = sqlcon.cursor()
    mod_id = int(input('Enter ID to modify: '))
    sal = int(input('Enter Salary: '))
    
    cur_mod.execute('update books set sal = %s where empno = %s'%(sal,mod_id))
    sqlcon.commit()
    print('Record Updated')

    cur_mod.close()

if __name__ == '__main__':
    main()