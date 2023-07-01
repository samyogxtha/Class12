import sqlite3
import random
import string
from tkinter import messagebox


def CheckPassword(password):
    return True if len(password) > 6 else False


def show_message(title, message):
    messagebox.showinfo(title, message)


def random_id():
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(8))


def RoomsDetails():
    conn = sqlite3.connect('hotel_booking_management.db')
    cursor = conn.cursor()

    cursor.execute(
        "CREATE TABLE IF NOT EXISTS roomsdetails (room_number TEXT PRIMARY KEY, price TEXT, booking_status TEXT, booking_id TEXT)")

    cursor.execute('SELECT * FROM roomsdetails')
    roomsdetails = cursor.fetchall()
    booked_rooms, non_booked_rooms = [], []
    for i in roomsdetails:
        if i[2]:
            booked_rooms.append(i)
        else:
            non_booked_rooms.append(i)
    conn.close()
    return booked_rooms, non_booked_rooms, roomsdetails


def CustomersDetails():
    conn = sqlite3.connect('hotel_booking_management.db')
    cursor = conn.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS customerdetails (booking_id TEXT PRIMARY KEY,customer_name TEXT,  no_of_people TEXT, mobile_number TEXT, address Text)")

    cursor.execute('SELECT * FROM customerdetails')
    customer_details = cursor.fetchall()
    conn.close()
    return customer_details


def AddRoom(room_number, price):
    try:
        conn = sqlite3.connect("hotel_booking_management.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO roomsdetails (room_number, price, booking_status, booking_id) VALUES (?, ?, ?, ?)",
                       (room_number, price, '', ''))
        conn.commit()
        conn.close()
        print('Room added')
    except sqlite3.Error as e:
        print('Error', e)
    finally:
        conn.close()


def BookRooms(booking_id, room_number):
    try:
        conn = sqlite3.connect('hotel_booking_management.db')
        c = conn.cursor()

        c.execute("UPDATE roomsdetails SET booking_status=?, booking_id=?  WHERE room_number=?",
                  ('booked', booking_id, room_number))
        conn.commit()
        print('Room booked')
        conn.close()
    except sqlite3.Error as e:
        print('Sqlite error', e)
    finally:
        conn.close()


def AddNewCustomer(booking_id, customer_name, no_of_people, mobile_number, address):
    CustomersDetails()
    try:
        conn = sqlite3.connect("hotel_booking_management.db")
        cursor = conn.cursor()
        cursor.execute("INSERT INTO customerdetails (booking_id, customer_name, no_of_people, mobile_number, address) VALUES (?, ?, ?, ?, ?)",
                       (booking_id, customer_name, no_of_people, mobile_number, address))
        conn.commit()
        conn.close()
        print('\nCustomer Added\n')
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        conn.close()


def UnBookRoom(room_number):
    try:
        conn = sqlite3.connect('hotel_booking_management.db')
        c = conn.cursor()

        c.execute("UPDATE roomsdetails SET booking_status=?, booking_id=?  WHERE room_number=?",
                  ('', '', room_number))
        conn.commit()
        print('Checkout successful')
        conn.close()
    except sqlite3.Error as e:
        print('Sqlite error', e)
    finally:
        conn.close()


password = input("""
Hi admin\n
please enter password
""")
while True:
    if CheckPassword(password):
        try:
            operation = int(input("""\n
1. New booking
2. Check out
3. Add room
4. Check all rooms available in CopyAssignment Hotel
5. Check available rooms
6. Exit\n"""))
        except Exception as e:
            print('\nEnter integer values only')
    else:
        print('Enter correct password!😤')
        password = input("Enter password again: ")
        continue
    if 1 <= operation <= 6:
        if operation == 1:
            allRooms = RoomsDetails()[2]
            print('Room No.    Price    Availability')
            for i in allRooms:
                print(' ', i[0], '   ', ' ', i[1], '   ',
                      ' available' if len(i[2]) == 0 else 'not available')
            customer_answer = input('Do you want to proceed?\n')
            if 'y' in customer_answer:
                from GenerateRandomID import random_id
                booking_id = random_id()
                customer_name = input('Enter your name: ')
                no_of_people = input('Number of people: ')
                mobile_number = input('Mobile number: ')
                address = input('Address: ')
                room_no_selected = input('Enter room no: ')
                available_rooms = [i[0] for i in RoomsDetails()[1]]
                if room_no_selected not in available_rooms:
                    print('Please select from available rooms only')
                    continue
                AddNewCustomer(booking_id, customer_name,
                               no_of_people, mobile_number, address)
                BookRooms(booking_id, room_no_selected)
            else:
                continue
        elif operation == 2:
            booked_rooms = RoomsDetails()[0]
            print('Booked Rooms')
            if len(booked_rooms) == 0:
                print('No booked rooms')
                continue
            for i in booked_rooms:
                print(i[0])
            room_no = input('Enter room no: ')
            booking_id = ''
            price = '1000'
            for i in booked_rooms:
                if i[0] == room_no:
                    price = i[1]
                    booking_id = i[3]
            allCustomers = CustomersDetails()
            no_of_people = 2
            for i in allCustomers:
                if i[0] == booking_id:
                    no_of_people = i[2]
            print('Thank you for visiting us!')
            print('Your total payable amount is:',
                  int(no_of_people)*int(price))
            wwwww = input('Enter upi id: ')
            print('Please accept payment request from your UPI app and pay', int(
                no_of_people)*int(price))
            print('Thank you, your payment is completed')
            UnBookRoom(room_no)
        elif operation == 3:
            print('\nSelected options is', operation)
            room_no = input('Enter room no: ')
            price = input('Enter room price: ')
            AddRoom(room_no, price)
        elif operation == 4:
            allRooms = RoomsDetails()[2]
            print('Room No.    Price    Availability')
            for i in allRooms:
                print(' ', i[0], '   ', ' ', i[1], '   ',
                      ' available' if len(i[2]) == 0 else 'not available')
        elif operation == 5:
            allRooms = RoomsDetails()[1]
            print('Room No.    Price    Availability')
            for i in allRooms:
                print(' ', i[0], '   ', ' ', i[1], '   ',
                      ' available' if len(i[2]) == 0 else 'not available')
        elif operation == 6:
            print('\n Thank you! Exiting...')
            break
    else:
        print("\nPlease enter values between 1 and 6 only")