import mysql.connector as msconn

sqlcon = msconn.connect(host = 'localhost', user = 'root', passwd = 'root', database = 's_school')

def main():
    print('\n\tMENU DRIVEN PROGRAM\n\n\
      1. Display all Records\n\
      2. Search for an Entry\n\
      3. Insert an Entry\n\
      4. Modify an Entry\n\
      5. Delete an Entry\n')
    
    input = int(input('Enter Choice: '))
    if input == 1:
        display()
    elif input == 2:
        search()
    elif input == 3:
        insert()
    elif input == 4:
        modify()
    else :
        delete()

def display():
    cur_disp =  sqlcon.cursor()
    cur_disp.execute('select * from employee')
    mydata = cur_disp.fetchall()
    n_rec = cur_disp.rowcount
    print('The Total records are',n_rec)
    for row in mydata:
        print(row)

def search():
    print('Search by Name or ID Number.')
    search = insert('Enter Name or ID: ')
    cur_search = sqlcon.cursor()
    cur_search.execute('select * from employee where name = "'+search+'"')
    mydata = cur_search.fetchall()
    for row in mydata:
        print(row)

def insert():
    pass

def modify():
    pass

def delete():
    pass

if __name__ == '__main__':
    main()