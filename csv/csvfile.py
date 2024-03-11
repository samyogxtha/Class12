import csv,tabulate

while True:
    print('\n\n----------MENU-DRIVEN-PROGRAM-CSV----------\n')
    print('''1. Display all Records
2. Input a record
3. Search for a record
4. Replace a record
5. Delete a Record
6. Total records in the file
0. Quit''')
    
    choice = int(input('\n\tEnter choice: '))
    print('\n\n')
    
    if choice == 1:
        with open('yo.csv') as cs:
            print('\tEmployee List')
            content = list(csv.reader(cs,delimiter=','))
            print(content)
            print(tabulate.tabulate(content,headers=['empno','emp Name','Salary'],tablefmt='mixed_grid'))
    elif choice == 2:
        with open('yo.csv','a',newline='') as cs:
            writer = csv.writer(cs,delimiter=',')
            writer.writerow([int(input('Enter Empno: ')),input('Enter Name: '),int(input('Enter Salary: '))])
    elif choice == 3:
        with open('yo.csv') as cs:
            content = list(csv.reader(cs,delimiter=','))
            search = input("Search by Employee Number: ")
            for i in content:
                if i[0] == search:
                    print(tabulate.tabulate([i],headers=['empno','emp Name','Salary'],tablefmt='mixed_grid'))
                    break
            else:
                print('\n\tEmployee not found')
    elif choice == 4:
        with open('yo.csv','r+',newline='') as cs:
            content = list(csv.reader(cs,delimiter=','))
            search = input("Update by Employee Number: ")
            for i in content:
                if i[0] == search:
                    print(tabulate.tabulate([i],headers=['empno','emp Name','Salary'],tablefmt='mixed_grid'))
                    writer = csv.writer(cs,delimiter=',')
                    i[1] = input('\nEnter Name: ')
                    i[2] = int(input('Enter Salary: '))
                    
                    cs.seek(0)
                    writer.writerows(content)
                    print('\n\tEmployee Updated')
                    break
            else:
                print('\n\tEmployee not found')
    elif choice == 5:
        cs = open('yo.csv','r+',newline='')
        content = list(csv.reader(cs,delimiter=','))
        search = input("Delete by Employee Number: ")
        for i in content:
            if i[0] == search:
                print(tabulate.tabulate([i],headers=['empno','emp Name','Salary'],tablefmt='mixed_grid'))
                cs.close()
                cs = open('yo.csv','w',newline='')
                writer = csv.writer(cs,delimiter=',')
                content.pop(content.index(i))
                writer.writerows(content)
                print('\n\tEmployee Deleted')
                cs.close()
                break
        else:
            print('\n\tEmployee not found')
            cs.close()
    else:break