import os

size_of_rec = 20

while True:
    print('''\n\n---------MENU-DRIVEN-PROGRAM----------
1. Add record
2. Display records
3. Search for record''')
    
    choice = int(input('Enter Choice:'))
    
    if choice == 1:
        with open('new_file.dat','ab') as file:
            inp = input('Enter Data: ')
            string = inp+' '*(size_of_rec-len(inp))
            string=string.encode()
            file.write(string)

    elif choice == 2:
        with open('new_file.dat') as file:
            content = file.read()

            x=file.tell()
            y=file.seek(0)
            while y < x:
                s = file.read(size_of_rec)
                print(s)
                y=file.tell()

            
    elif choice == 3:
        with open('new_file.bin') as file:
            content = file.read()
            #content = content.decode()

            k = input('Enter Data to search: ')

            ind = content.find(k)

            pos = ind//size_of_rec

            print(pos)

            file.seek(ind)
            
            dat= file.read(size_of_rec)
            #dat = dat.decode()

            print(pos+1,dat)
    else:break
