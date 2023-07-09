import datetime
from tabulate import tabulate
import mysql.connector as msconn #pip install mysql-connector-python

def rooms():
    pass

def customer():
    pass

def bookings():
    pass

def payments():
    pass


def main():
    while True:
        print('\n')
        print('='*40,'\n\n\tHOTEL MANAGER\n')
        print('='*40,'\n\
        1. Rooms\n\
        2. Customer\n\
        3. Bookings\n\
        4. Payments\n\
        0. Exit\n')

        choice = int(input('Enter Choice: '))
        print('\n')
        if choice == 1:
            rooms()
        elif choice == 2:
            customer()
        elif choice == 3:
            bookings()
        elif choice == 4:
            payments()
        else :
            break

if __name__ == '__main__':
    sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'hotel') 
    main()
    sqlcon.close()