'''Write a menu-driven program in Python to: 

Create a binary file named employee.dat and insert records with the contents (emp_id, emp_name, department, salary) 

Read and display all records from the file. 

Delete a record in the file using emp_id'''

import pickle,tabulate

def insert():
    with open('employee.dat','+ab') as bf:
        emp_id = int(input('enter emp id: '))
        emp_name = input('enter emp name: ')
        dept = input('enter department: ')
        sal = int(input('enter salary: '))
        pickle.dump([emp_id,emp_name,dept,sal],bf)

def display():
    with open('employee.dat','rb') as bf:
        totrec = []
        while True:
            try:totrec.append(pickle.load(bf))
            except:break
        print(tabulate.tabulate(totrec,headers=['emp_id','emp_name','department','salary']),'\n')

def delete():
    with open('employee.dat','rb') as bf:
        totrec = []
        while True:
            try:totrec.append(pickle.load(bf))
            except:break
    id = int(input('enter emp_id to delete: '))
    for i in totrec:
        if i[0]==id:
            totrec.remove(i)
    with open('employee.dat','wb') as bf:
        pickle.dump(totrec,bf)



while True:
    print('''------------MENU-DRIVEN-PROGRAMME------------
    1. Insert a record
    2. Display all records
    3. Delete a record
    0. Exit''')
    ch = input('enter choice: ')
    if ch == '1':insert()
    elif ch == '2':display()
    elif ch == '3':delete()
    elif ch == '0':break
    else:print('Please insert a valid choice')
