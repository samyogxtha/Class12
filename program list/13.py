'''Create an EMPLOYEE table using MySQL with the following fields:
Emp_no, Emp_Name, Designation, Department, Salary
Write a Python program to connect with the above table and do the following functions:
a.	Add employee details
b.	Display all employees
c.	Delete an employee
d.	Search for an employee
e.	Modify the details of an employee'''

from tabulate import tabulate
import mysql.connector as msconn

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy',database = 'employee')

cur = sqlcon.cursor()

print('\n\n----------MENU-DRIVEN-PROGRAM----------\n')
print('''1. Add employee details
2. Display all employees
3. Delete an employee
4. Search for an employee
5. Modify the details of an employee
0. Quit''')
    
while True:
    choice = int(input('\n\tEnter Choice: '))
    if choice == 1:
        empno = int(input('\nEnter Employee Number: '))
        name = input('Enter Name: ')
        des = input('Enter Designation: ')
        dept = input('Enter Department: ')
        sal = int(input('Enter Salary: '))
        cur.execute(f'insert into employee values ({empno},"{name}","{des}","{dept}",{sal})')
        sqlcon.commit()
        print('\n\t--Employee added Succesfully--')

    elif choice == 2:
        cur.execute('select * from employee')
        dat = cur.fetchall()
        if dat == []:print('\n\t--Table Empty--')
        else:print('\n',tabulate(dat,headers = ['Emp_no','Emp_name','Designation','Department','Salary'],tablefmt='mixed_grid'))

    elif choice == 3:
        del_num = input('\nEnter Employee ID to delete: ')
        try:
            cur.execute(f'delete from employee where emp_no = {del_num}')
            sqlcon.commit()
            print('\n\t--Employee Deleted--')
        except:print('\n\t--Employee Not Found--')
        
    elif choice == 4:
        search = int(input('Search by Employee Number: '))
        cur.execute(f'select * from employee where emp_no = {search}')
        dat = cur.fetchall()
        if dat == []:print('\n\t--Employee Not Found--')
        else:print('\n',tabulate(dat,headers = ['Emp_no','Emp_name','Designation','Department','Salary'],tablefmt='mixed_grid'))

    elif choice == 5:
        empno = int(input('Enter Employee Number to modify: '))
        cur.execute(f'select * from employee where emp_no = {empno}')
        dat = cur.fetchall()
        if dat == []:print('\n\t--Employee Not Found--')
        else:
            name = input('Enter Name: ')
            des = input('Enter Designation: ')
            dept = input('Enter Department: ')
            sal = int(input('Enter Salary: '))
            cur.execute(f'update employee set emp_name="{name}",designation="{des}",department="{dept}",salary={sal} where emp_no = {empno}')
            sqlcon.commit()
            print('\n\t--Details Modified Succesfully--')
    else:break