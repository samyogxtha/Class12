from tkinter import *
from tkinter import ttk
from customtkinter import *
from PIL import ImageTk,Image #pip install pillow
from tkinter import messagebox
import datetime
import mysql.connector as msconn #pip install mysql-connector-python

def db_check():
    global sqlcon
    cur = sqlcon.cursor()
    cur.execute('show databases')
    db = cur.fetchall()
    dbs = []
    for i in db:
        dbs.append(i[0])
    if 'hotel' not in dbs:
            cur.execute('CREATE DATABASE hotel')
            sqlcon.commit()
            
            sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')
            cur = sqlcon.cursor()
            cur.execute('create table Books(slno int auto_increment UNIQUE, ISBNo int primary key, Book_Name varchar(50) not null, Author varchar(30) not null, Publisher varchar(30) not null, Genre varchar(30) not null, Price int not null, No_of_copies int)')
            cur.execute('create table Customers(slno int auto_increment UNIQUE, Cust_ID int primary key, Cust_Name varchar(50) not null, Age int(3) , Date_Of_Birth date,Address varchar(30) not null, Mobile bigint not null, Email varchar(50) not null)')
            cur.execute('create table Issue(slno int auto_increment primary key, Date_of_issue DATETIME default now(),ISBno INT NOT NULL, Book_Name varchar(50) not null, Cust_ID int not null, Cust_Name varchar(30) not null,constraint mykey foreign key(ISBNo) references books(ISBNo),constraint mykey2 foreign key(Cust_ID) references customers(Cust_ID))')
            cur.execute('create table Returns(slno int auto_increment Primary key, Date_of_return DATETIME default now(),ISBno int NOT NULL, Cust_ID int not null,Fine_Amount decimal(10,2),paid char(1) ,constraint mykey3 foreign key(ISBNo) references books(ISBNo),constraint mykey4 foreign key(Cust_ID) references customers(cust_id))')
            sqlcon.commit()
            cur.close()
    else:
        cur.close()
        sqlcon.close()
        sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'library')

def rooms():
    pass

def customer():
    pass

def book():
    pass

def check_out():
    pass


def main():
    while True:
        print('\n')
        print('='*40,'\n\n\tHOTEL BOOKINGS\n')
        print('='*40,'\n\
        1. New Booking\n\
        2. Check out\n\
        3. Exit\n')

        choice = int(input('Enter Choice: '))
        print('\n')
        if choice == 1:
            book()
        elif choice == 2:
            check_out()
        else :
            break

if __name__ == '__main__':
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root')
    db_check() 
    main()
    sqlcon.close()