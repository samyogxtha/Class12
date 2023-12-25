'''1. Write a menu driven program to create a CSV file with the following details.
Emp_No, Emp_Name, Job, Department, Salary
Add the following menus to the program:
a) Write data to the file
b) Display all records from the file
c) Search for a particular employee using employee number
d) Modify a record
e) Delete a record
f) Display total records in the file'''\

import csv,tabulate,sys

print('\n\n----------MENU-DRIVEN-PROGRAM-CSV----------\n')
print('''1. Display all Records
2. Input a record
3. Search for a record
4. Replace a record
5. Delete a Record
6. Total records in the file
0. Quit''')
    
while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')
    
    if choice == 1:
        with open('employee.csv') as cs:
            content = list(csv.reader(cs,delimiter=','))
            if content!=[]:
                print('\tEmployee List')
                print(tabulate.tabulate(content,headers=['Emp_No', 'Emp_Name', 'Job', 'Department', 'Salary'],tablefmt='mixed_grid'))
            else:sys.stderr.write('\nFile Empty\n')
    elif choice == 2:
        with open('employee.csv','a',newline='') as cs:
            writer = csv.writer(cs,delimiter=',')
            writer.writerow([int(input('Enter Empno: ')),input('Enter Name: '),input('Enter Job: '),input('Enter Department: '),int(input('Enter Salary: '))])
            print('\nRecord Added\n')
    elif choice == 3:
        with open('employee.csv') as cs:
            content = list(csv.reader(cs,delimiter=','))
            search = input("Search by Employee Number: ")
            for i in content:
                if i[0] == search:
                    print(tabulate.tabulate([i],headers=['Emp_No', 'Emp_Name', 'Job', 'Department', 'Salary'],tablefmt='mixed_grid'))
                    break
            else:
                sys.stderr.write('\n\tEmployee not found\n')
    elif choice == 4:
        with open('employee.csv','r+',newline='') as cs:
            content = list(csv.reader(cs,delimiter=','))
            search = input("Update by Employee Number: ")
            for i in content:
                if i[0] == search:
                    print(tabulate.tabulate([i],headers=['Emp_No', 'Emp_Name', 'Job', 'Department', 'Salary'],tablefmt='mixed_grid'))
                
                    i[1] = input('\nEnter Name: ')
                    i[2] = input('Enter Job: ')
                    i[3] = input('Enter Department: ')
                    i[4] = input('Enter Salary: ')
                    
                    with open('employee.csv','w',newline='') as f:
                        writer = csv.writer(f,delimiter=',')
                        for i in content:
                            writer.writerow(i)
                    print('\n\tEmployee Updated')
                    break
            else:
                sys.stderr.write('\n\tEmployee not found\n')
    elif choice == 5:
        cs = open('employee.csv','r+',newline='')
        content = list(csv.reader(cs,delimiter=','))
        search = input("Delete by Employee Number: ")
        for i in content:
            if i[0] == search:
                print(tabulate.tabulate([i],headers=['Emp_No', 'Emp_Name', 'Job', 'Department', 'Salary'],tablefmt='mixed_grid'))
                cs.close()
                cs = open('employee.csv','w',newline='')
                writer = csv.writer(cs,delimiter=',')
                content.pop(content.index(i))
                writer.writerows(content)
                print('\n\tEmployee Deleted')
                cs.close()
                break
        else:
            sys.stderr.write('\n\tEmployee not found\n')
            cs.close()
    elif choice == 6:
        with open('employee.csv') as cs:
            print('\tEmployee List')
            content = list(csv.reader(cs,delimiter=','))
            if content!=[]:print(f'The total records in the file is {len(content)}')
            else:sys.stderr.write('File Empty')  
    else:break