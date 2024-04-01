'''a)	Write a menu-driven program in Python to:
i.	Create a binary file named employee.dat and insert records with the contents (emp_id, emp_name, department, salary)
ii.	Read and display all records from the file.
iii.	Search for a record in the file using emp_id'''

import pickle,tabulate

def add_rec():
    try:
        with open('employee.dat','ab') as file:
            eid = int(input('\nEnter e_id: '))
            ename = input('Enter Name: ')
            dept = input('Enter Department: ')
            sal = int(input('Enter Salary: '))
            pickle.dump([eid,ename,dept,sal],file)
            print('\n\t-Record-Added-Successfully-')
    except:print('\n\t-File-Not-Found-')

def disp_rec():
    try:
        with open('employee.dat','rb') as file:
            dat = []
            while True:
                try:dat.append(pickle.load(file))
                except:break
            if dat != []:
                print(tabulate.tabulate(dat,headers=['emp_id','emp_name','Departmant','Salary'],tablefmt='mixed_grid'))
            else:print('\n\t-File-Empty-')
    except:print('\n\t-ERROR-')

def search_rec():
    try:
        with open('employee.dat','rb') as file:
            dat = []
            while True:
                try:dat.append(pickle.load(file))
                except:break
            search = int(input('Enter e_id to search: '))
            if dat != []:
                for i in dat:
                    if i[0] == search:
                        print(tabulate.tabulate([i],headers=['emp_id','emp_name','Departmant','Salary'],tablefmt='mixed_grid'))
                        break
                else:print('\n\t-Record-Not-Found-')
            else:print('\n\t-File-Empty-')
    except:print('\n\t-ERROR-')

while True:
    print('''\n\n---------MENU-DRIVEN-PROGRAM----------
1. Add record
2. Display records
3. Search for record''')
    
    choice = int(input('Enter Choice:'))
    
    if choice == 1:
        add_rec()
    elif choice == 2:
        disp_rec()
    elif choice == 3:
        search_rec()
    else:break