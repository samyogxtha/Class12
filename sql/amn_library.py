import mysql.connector as mys
mycon=mys.connect(host='localhost', user='root', passwd='samy', database='library')
def display_all_books():
    mycursor=mycon.cursor()
    mycursor.execute("select* from books")
    mydata=mycursor.fetchall()
    nrec=mycursor.rowcount
    print("Total records fetched are", nrec)
    for row in mydata:
        print(row)
def display_all_customers():
    mycursor=mycon.cursor()
    mycursor.execute("select* from customer")
    mydata=mycursor.fetchall()
    nrec=mycursor.rowcount
    print("Total records fetched are", nrec)
    for row in mydata:
        for r in row:
            print(r)
def borrow():
    mycursor=mycon.cursor()
    print("Borrow a Book")
    ans='y'
    while ans.lower()=="y":
        sno=input('Enter serial number:')
        cno=int(input('Enter Customer ID:'))
        cname='select Custm_Name from customer where Custm_ID={}'. format(cno)
        mycursor.execute(cname)
        cname=mycursor.fetchall()[0][0]
        import datetime
        date = datetime.datetime.now()
        ISBN=input("Enter ISBN:")
        bname='select Book_Name from books where ISBN="{}"'. format(ISBN)
        mycursor.execute(bname)
        bname=mycursor.fetchone()
        query='insert into issue values({}, "{}", "{}", "{}", {}, "{}")'. format(sno, date, ISBN, bname, cno, cname)
        mycursor.execute(query)
        copies_no='select No_of_Copies from books where ISBN="{}"'. format(ISBN)
        mycursor.execute(copies_no)
        data=mycursor.fetchone()
        data2=data[0]
        data3=data2-1
        mycursor.execute(query)
        mycon.commit()
        query1='update books set No_of_copies={} where ISBN={}'. format(data3, ISBN)
        mycursor.execute(query1)
        mycon.commit()
        query2='insert into returnes(SNO, Due_Date, ISBN, Custm_ID) values( {}, dateadd(week, 3, {}), "{}",{})'. format( sno, date, ISBN, cno)
        mycursor.execute(query2)
        mycon.commit()
        print("------------------RECORD SAVED---------------")
        ans=input("Do you want to borrow more books?(y/n)")
def return_book():
    mycursor=mycon.cursor()
    print("Return a Book")
    cno=int(input("Enter Customer ID:"))
    ISBN=input('Enter ISBN:')
    query='select * from returnes where Custm_ID={} and ISBN="{}"'. format(cno, ISBN)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print("------------------RECORD FOUND---------------")
        answer=input("Are you sure you want to return the book?(y/n)")
        if answer.lower()=='y':
            import datetime
            r_date = datetime.datetime.now()
            query='insert into returnes (Date_returned) values("{}")'. format(r_date)
            mycursor.execute(query)
            mycon.commit()
            copies_no='select No_of_Copies from books where ISBN="{}"'. format(ISBN)
            mycursor.execute(copies_no)
            data=mycursor.fetchone()
            data2=data[0]
            data3=data2+1
            query1 ='update books set No_of_copies={} where ISBN={}'. format(data3, ISBN)
            mycursor.execute(query1)
            mycon.commit()
            query1='select Due_date from returnes where where ISBN="{}" and custm_id={}'. format(ISBN, cno)
            mycursor.execute(query1)
            data=mycursor.fetchone()
            query2='select datediff("{}", "{}")'. format(data, r_date)
            mycursor.execute(query2)
            data2=mycursor.fetchone()
            if data2<=21:
                query3='insert into returnes(Fine_Amount, Payment_Status) values(NULL, NULL)'
                mycursor.execute(query3)
                mycon.commit
            else:
                query3='select price from books where ISBN="{}"'. format(ISBN)
                mycursor.execute(query3)
                data3=mycursor.fetchone()+(data2*2)
                ans=("You have returned the book after the due date and hence are subject to a fine. Do you want to Pay the fine now?(y/n)")
                if ans.lower=='y':
                    query4='insert into returnes(Fine_Amount, Payment_Status) values({}, "{}")'. format(data3, ans.upper())
                    mycursor.execute(query4)
                    mycon.commit()
                else:
                    query4='insert into returnes(Fine_Amount, Payment_Status) values({}, "{}")'. format(data3,'N')
                    mycursor.execute(query4)
                    mycon.commit()
def add_books():
    mycursor=mycon.cursor()
    print("Welcome to Book Data Entry")
    ans='y'
    while ans.lower()=="y":
        sno=int(input('Enter Serial Number:'))
        isbn=input("Enter ISBN:")
        book_name=input("Enter Book's Name:")
        author=(input("Enter Author's Name:"))
        publisher=input("Enter Publisher's Name:")
        category=input("Enter Book Category:")
        price=int(input("Enter Book Price:"))
        copies_no=int(input("Enter Number of Copies:"))
        query='insert into books values({}, "{}", "{}", "{}", "{}", "{}", {}, {})'. format(sno, isbn, book_name, author, publisher, category, price, copies_no)
        mycursor.execute(query)
        mycon.commit()
        print("------------------RECORD SAVED---------------")
        ans=input("Do you want to add more?(y/n)")
def remove_books():
    mycursor=mycon.cursor()
    isbn=(input("Enter ISBN:"))
    query='delete from books where ISBN="{}"'. format(isbn)
    mycursor.execute(query)
    query='select * from books where ISBN="{}"'. format(isbn)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data==None:
        print("-----------------------------RECORD SUCCESSFULLY DELETED------------------------")
    else:
        print("-----------------------------RECORD NOT FOUND--------------------------")
def add_customers():
    mycursor=mycon.cursor()
    print("Welcome to Customer Data Entry")
    ans='y'
    while ans.lower()=="y":
        sno=int(input('Enter Serial Number:'))
        Custm_ID=int(input("Enter Custm_ID:"))
        Custm_Name=input("Enter Customer Name:")
        age=int(input("Enter Customer's Age:"))
        dob=(input("Enter Customer's D.O.B:"))
        address=input("Enter Customer's Address:")
        mobile=int(input("Enter Customer's Mobile Number:"))
        email_id=(input("Enter Customer's Email_ID:"))
        query='insert into customer values({}, {}, "{}", {}, "{}", "{}", {}, "{}")'. format(sno, Custm_ID, Custm_Name, age, dob, address, mobile, email_id)
        mycursor.execute(query)
        mycon.commit()
        print("------------------RECORD SAVED---------------")
        ans=input("Do you want to add more?(y/n)")
def remove_customers():
    mycursor=mycon.cursor()
    custm_id=int(input("Enter Customer ID:"))
    query='delete from customer where Custm_ID={}'. format(custm_id)
    mycursor.execute(query)
    query='select * from customer where Custm_ID={}'. format(custm_id)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data==None:
        print("-----------------------------RECORD SUCCESSFULLY DELETED------------------------")
    else:
        print("-----------------------------RECORD NOT FOUND--------------------------")
def search_books():
    mycursor=mycon.cursor()
    isbn=(input("Enter ISBN:"))
    query='select * from books where ISBN="{}"'. format(isbn)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print("-----------------------------RECORD FOUND------------------------")
        for row in data:
            print(row)
    else:
        print("-----------------------------RECORD NOT FOUND--------------------------")
def search_customers():
    mycursor=mycon.cursor()
    custm_id=int(input("Enter Custm_ID:"))
    query='select * from customer where Custm_ID={}'. format(custm_id)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print("-----------------------------RECORD FOUND------------------------")
        for row in data:
            print(row)
    else:
        print("-----------------------------RECORD NOT FOUND--------------------------")
def update_books():
    mycursor=mycon.cursor()
    print("Welcome to Book Data Update Screen")
    isbn=(input("Enter ISBN:"))
    query='select * from Books where ISBN={}'. format(isbn)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print("------------------RECORD FOUND---------------")
        for row in data:
            print(row)
        answer=input("Are you sure you want to update price?(y/n)")
        if answer.lower()=='y':
            price=int(input("Enter Updated Price:"))
            query="update books set Price={} where ISBN='{}'". format(price,isbn)
            mycursor.execute(query)
            mycon.commit()
            print("------------------RECORD UPDATED---------------")
    else:
        print("-------------------RECORD NOT FOUND--------------------")
def update_customers():
    mycursor=mycon.cursor()
    print("Welcome to Customer Data Update Screen")
    custm_id=int(input("Enter Custm_ID:"))
    query='select * from customer where Custm_ID={}'. format(custm_id)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        print("------------------RECORD FOUND---------------")
        for row in data:
            print(row)
        ans='y'
        while ans.lower()=='y':
            print("1. Update Age")
            print("2. Update Address")
            print("3. Update Mobile Number")
            print("4. Update Email_ID")
            answer=input("Which of the above do you want to update?")
            if answer==1:
                age=int(input("Enter Updated Age:"))
                query="update customer set Age={} where Custm_ID={}". format(age, custm_id)
                mycursor.execute(query)
                mycon.commit()
                print("------------------RECORD UPDATED---------------")
            elif answer==2:
                address=(input("Enter Updated Address:"))
                query="update customer set Address={} where Custm_ID={}". format(address, custm_id)
                mycursor.execute(query)
                mycon.commit()
                print("------------------RECORD UPDATED---------------")
            elif answer==3:
                mobile=int(input("Enter Updated Mobile Number:"))
                query="update customer set Mobile={} where Custm_ID={}". format(mobile, custm_id)
                mycursor.execute(query)
                mycon.commit()
                print("------------------RECORD UPDATED---------------")
            elif answer==4:
                email_id=(input("Enter Updated Email_ID:"))
                query="update customer set Email_ID={} where Custm_ID={}". format(email_id, custm_id)
                mycursor.execute(query)
                mycon.commit()
                print("------------------RECORD UPDATED---------------")
            ans=input("Do you want to continue?(y/n)")
    else:
        print("-------------------RECORD NOT FOUND--------------------")
print("Menu Driven Program")
c_e=input('Are you a Employee or a Customer?(c/e)')
if c_e.lower()=="c":
    answer='y'
    while answer.lower()=='y':
          print("_____________________________")
          print("1.DISPLAY ALL BOOKS")
          print("2.DISPLAY ALL CUSTOMERS")
          print("3.BORROW A BOOK")
          print("4.RETURN A BOOK")
          print("_____________________________")
          c=int(input("Enter your choice-"))
          print("_____________________________")
          if c==1:
              display_all_books()
          elif c==2:
              display_all_customers()
          elif c==3:
              borrow()
          elif c==4:
              return_book()
          print("_____________________________")
          answer=input("Do you want to continue?(y/n)")
          print("_____________________________")
else:
    mycursor=mycon.cursor()
    eno=int(input("Enter Employee number:"))
    query='select * from employee where emp_no={}'. format(eno)
    mycursor.execute(query)
    data=mycursor.fetchone()
    if data!=None:
        answer='y'
        while answer.lower()=='y':
              print("_____________________________")
              print("1.DISPLAY ALL BOOKS")
              print("2.DISPLAY ALL CUSTOMERS")
              print("3.ADD BOOKS")
              print("4.REMOVE BOOKS")
              print("5.ADD CUSTOMERS")
              print("6.REMOVE CUSTOMERS")
              print("7.SEARCH FOR BOOKS")
              print("8.SEARCH FOR CUSTOMERS")
              print("9.UPDATE BOOK DETAILS")
              print("10.UPDATE CUSTOMER DETAILS")
              print("_____________________________")
              c=int(input("Enter your choice-"))
              print("_____________________________")
              if c==1:
                  display_all_books()
              elif c==2:
                  display_all_customers()
              elif c==3:
                  add_books()
              elif c==4:
                  remove_books()
              elif c==5:
                  add_customers()
              elif c==6:
                  remove_customers()
              elif c==7:
                  search_books()
              elif c==8:
                  search_customers()
              elif c==9:
                  update_books()
              elif c==10:
                  update_customers()
              print("_____________________________")
              answer=input("Do you want to continue?(y/n)")
              print("_____________________________")
        else:
            print("----------------EMPLOYEE ID NOT VALID--------------------")