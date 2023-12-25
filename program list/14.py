'''Create a table “STUDENTS” using MySQL with the following fields:
S_ID, S_NAME, AGE, DOB, GRADE, CLASS_TEACHER
Write a Python program to connect with the above table and do the following functions:
a.	Add students details
b.	Display all students
c.	Remove a student
d.	Count and display number of students in a particular grade
e.	Modify the details.'''

import tabulate,sys
import mysql.connector as msconn

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy',database = 'student')

cur = sqlcon.cursor()

print('\n--------Menu-Driven-Program--------\n')
print('''1. Enter Student Details 
2. Display all students
3. Delete a student
4. Count and display number of students in a particular grade
5. Modify the details of a students
0. Quit
''')

while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')

    if choice == 1:
        try:
            id = int(input('Enter Roll Number: '))
            name = input('Enter Student Name: ')
            age = input('Enter Age: ')
            dob = input('Enter DOB (yyyy-mm-dd): ')
            grade = int(input('Enter Grade: '))
            teach = input('Enter Class Teacher: ')

            cur.execute(f'insert into student values ({id},"{name}",{age},"{dob}",{grade},"{teach}")')
            sqlcon.commit()
            print('\n--Record added Succesfully--')
        except:sys.stderr.write('\n--ERROR Try Again--\n')
        
    elif choice == 2:
        cur.execute('select * from student')
        dat = cur.fetchall()
        if dat == []:sys.stderr.write('\n\t--Table Empty--\n')
        else:print(tabulate.tabulate(dat,headers = ['S_ID', 'STUDENT NAME', 'AGE', 'DOB', 'GRADE', 'CLASS TEACHER'],tablefmt='mixed_grid'))

    elif choice == 3:
        del_num = input('\nEnter Student ID to delete: ')
        try:
            cur.execute(f'delete from student where s_id = {del_num}')
            sqlcon.commit()
            print('\n\t--Student Record Deleted--')
        except:sys.stderr.write('\n\t--Student Not Found--\n')

    elif choice == 4:
        grade = int(input('Enter Grade: '))
        cur.execute(f'select*from student where grade = {grade}')
        dat = cur.fetchall()

        if dat == []:sys.stderr.write('\n\t--Grade Not Found--\n')
        else:print(tabulate.tabulate(dat,headers = ['S_ID', 'STUDENT NAME', 'AGE', 'DOB', 'GRADE', 'CLASS TEACHER'],tablefmt='mixed_grid'))


    elif choice == 5:
        id = int(input('Enter Student Number to modify: '))
        cur.execute(f'select * from student where s_id = {id}')
        dat = cur.fetchall()
        if dat == []:sys.stderr.write('\n\t--Student Not Found--\n')
        else:
            try:
                name = input('Enter Student Name: ')
                age = input('Enter Age: ')
                dob = input('Enter DOB (yyyy-mm-dd): ')
                grade = int(input('Enter Grade: '))
                teach = input('Enter Class Teacher: ')
                
                cur.execute(f'update student set S_ID = {id},S_NAME = "{name}",AGE = {age},DOB = "{dob}",GRADE = {grade},CLASS_TEACHER = "{teach}" where S_ID = {id}')
                sqlcon.commit()
                print('\n\t--Details Modified Succesfully--')
            except:sys.stderr.write('\n\t--ERROR Try Again--\n')
    else:break