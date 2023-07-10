#from tkinter import *
#from tkinter import ttk
#from customtkinter import *
from PIL import ImageTk,Image #pip install pillow
from tkinter import messagebox
import datetime
import mysql.connector as msconn #pip install mysql-connector-python

def db_check():
    global sqlcon
    cur = sqlcon.cursor()
    cur.execute('CREATE DATABASE IF NOT EXISTS hotel')
    sqlcon.commit()
    cur.close()
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 'hotel')
    cur = sqlcon.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS customer(\
            slno	INT AUTO_INCREMENT UNIQUE ,\
            cust_id	INT PRIMARY KEY ,\
            cust_name	VARCHAR(50) ,\
            age	INT ,\
            dob	DATE ,\
            address	VARCHAR(50) ,\
            mobile	INT ,\
            email	VARCHAR(50))')
    cur.execute('CREATE TABLE IF NOT EXISTS rooms(\
            room_no      INT  PRIMARY KEY AUTO_INCREMENT ,\
            availability CHAR(1) NOT NULL ,\
            type         VARCHAR(10) NOT NULL ,\
            ac           CHAR(1) ,\
            tv           CHAR(1) ,\
            wifi         CHAR(1) ,\
            price        INT  NOT NULL)')
    cur.execute("INSERT IGNORE INTO rooms VALUES\
            (1,'y','single',NULL,NULL,'y',1000),\
            (2,'y','single','y','y',NULL,1100),\
            (3,'y','single',NULL,'y','y',1200),\
            (4,'y','single','y',NULL,'y',1300),\
            (5,'y','single','y','y','y',1400),\
            (6,'y','double',NULL,NULL,'y',2000),\
            (7,'y','double','y','y',NULL,2100),\
            (8,'y','double',NULL,'y','y',2200),\
            (9,'y','double','y',NULL,'y',2300),\
            (10,'y','double','y','y','y',2400),\
            (11,'y','triple',NULL,NULL,'y',3000),\
            (12,'y','triple','y','y',NULL,3100),\
            (13,'y','triple',NULL,'y','y',3200),\
            (14,'y','triple','y',NULL,'y',3300),\
            (15,'y','triple','y','y','y',3400),\
            (16,'y','quad',NULL,NULL,'y',4000),\
            (17,'y','quad','y','y',NULL,4100),\
            (18,'y','quad',NULL,'y','y',4200),\
            (19,'y','quad','y',NULL,'y',4300),\
            (20,'y','quad','y','y','y',4400)")
    cur.execute('CREATE TABLE IF NOT EXISTS bookings(\
            booking_id    INT  PRIMARY KEY AUTO_INCREMENT,\
            cust_id       INT  NOT NULL ,\
            room_no        INT  NOT NULL ,\
            checkin_date  DATE  NOT NULL ,\
            checkout_date DATE,\
            no_of_days    INT  NOT NULL ,\
            check_inout   CHAR(1) NOT NULL ,\
            FOREIGN KEY (cust_id)  REFERENCES customer (cust_id),\
            FOREIGN KEY (room_no) REFERENCES rooms     (room_no))')
    cur.execute('CREATE TABLE IF NOT EXISTS payments(\
            slno            INT  NOT NULL PRIMARY KEY,\
            cust_id         INT  NOT NULL ,\
            room_no         INT  NOT NULL ,\
            checkin_date    DATE  NOT NULL ,\
            checkout_date   DATE  NOT NULL ,\
            days_overstayed INT ,\
            fine            INT ,\
            price           INT NOT NULL ,\
            paid            CHAR(1) NOT NULL ,\
            FOREIGN KEY (cust_id)  REFERENCES customer  (cust_id) ,\
            FOREIGN KEY (room_no)  REFERENCES rooms     (room_no))')
    sqlcon.commit()
    cur.close()

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