'''1.pya)Write a menu-driven program in Python to:
    i.  Create a binary file named employee.dat and insert records with the contents (emp_id, emp_name, department, salary)
    ii. Read and display all records from the file.
    iii.Search for a record in the file using emp_id'''

import pickle,tabulate

def insert_rec():
    try:
        with open('employee.dat','ab') as file:
            eid = int(input('Enter emp_id: '))
            name = input('Enter Name: ')
            dept = input('Enter Department: ')
            sal = int(input('Enter Salary: '))
            pickle.dump([eid,name,dept,sal],file)
            print('\n\t-Record-Added-')
    except:print('\n\t-ERROR-')

def disp_rec():
    with open('employee.dat','rb') as file:
        rec = []
        while True:
            try:rec.append(pickle.load(file))
            except:break
        if not rec:
            print('\n\t-File-Empty-')
        else:
            print('\nEmployees:')
            print(tabulate.tabulate(rec,headers=['emp_id', 'emp_name', 'department', 'salary'],tablefmt='mixed_grid'))

def search_rec():
    with open('employee.dat','rb') as file:
        rec = []
        while True:
            try:rec.append(pickle.load(file))
            except:break
        search = int(input('Enter emp_id to search: '))
        if not rec:
            print('\n\t-File-Empty-')
        else:
            for i in rec:
                if search == i[0]:
                    print('\nEmployee:')
                    print(tabulate.tabulate([i],headers=['emp_id', 'emp_name', 'department', 'salary'],tablefmt='mixed_grid'))
                    break

while True:
    print('\n\t------MENU-DRIVEN-PROGRAM------')
    print('''1. Insert Records
2. Display all Records
3. search for a record
0. Quit''')
    choice = int(input('\n\tEnter Choice: '))

    if choice == 1:
        insert_rec()
    elif choice == 2:
        disp_rec()
    elif choice == 3:
        search_rec()
    elif choice == 0:
        break
    else:
        print('\n\t-Enter-Valid-Choice-')
