from tkinter import *
from tkinter import ttk
from PIL import ImageTk,Image
from tkinter import messagebox
import datetime
import mysql.connector as msconn #pip install mysql-connector-python

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
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel') 
    main()
    sqlcon.close()