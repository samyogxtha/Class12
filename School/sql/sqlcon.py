import mysql.connector as msconn #pip install mysql-connector-python

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'samy', database = 'school')

def main():
    while True:
        print('\n\tMENU DRIVEN PROGRAM\n\n\
        1. Display all Records\n\
        2. Search for an Entry\n\
        3. Insert an Entry\n\
        4. Modify an Entry\n\
        5. Delete an Entry\n\
        6. Exit\n')
        
        choice = int(input('Enter Choice: '))
        if choice == 1:
            display()
        elif choice == 2:
            search()
        elif choice == 3:
            insert()
        elif choice == 4:
            modify()
        elif choice == 5:
            delete()
        else :
            break

def display():
    cur_disp =  sqlcon.cursor()
    cur_disp.execute('select * from employee order by empno')
    mydata = cur_disp.fetchall()
    n_rec = cur_disp.rowcount
    print('\nThe Total records are',n_rec)
    for row in mydata:
        print(row[0],'|',row[1],'|',row[2],'|',row[3])
    print('\n')

def search():
    ni = input('\nSearch by Name or ID Number (n/i): ')
    cur_search = sqlcon.cursor()
    
    if ni in 'nN':
        search_name = input('Enter Name: ')
        cur_search.execute('select * from employee where name = "'+search_name+'"')
    else:
        search_num = int(input('Enter ID: '))
        cur_search.execute('select * from employee where empno = '+str(search_num))

    data_search = cur_search.fetchall()
    print('\n')
    if data_search != None:
        for row in data_search:
            print(row[0],'|',row[1],'|',row[2],'|',row[3])
        print('\n')
    else:
        print('No records found.\n')

    cur_search.close()

def insert():
    cur_insert = sqlcon.cursor()

    empno = int(input('\nEnter Employee ID: '))
    name = input('Enter Name: ')
    dept = input('Enter Department: ')
    sal = int(input('Enter Salary: '))

    cur_insert.execute('insert into employee values(%s,"%s","%s",%s)'%(empno,name,dept,sal))
    sqlcon.commit()
    print('\nRecord Saved')
    cur_insert.close()

def modify():
    cur_mod = sqlcon.cursor()
    mod_id = int(input('Enter ID to modify: '))
    sal = int(input('Enter Salary: '))
    
    cur_mod.execute('update employee set sal = %s where empno = %s'%(sal,mod_id))
    sqlcon.commit()
    print('Record Updated')

    cur_mod.close()

def delete():
    cur_del =  sqlcon.cursor()
    del_num = input('Enter ID to delete: ')
    cur_del.execute('delete from employee where empno = '+str(del_num))
    print('\nRecord Deleted.\n')
    cur_del.close()

if __name__ == '__main__':
    main()