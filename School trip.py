def main():
    print('\n\n')
    while True:
        n_students = int(input('Enter the number of Students: '))
        if 0 <= n_students <= 45:
            break
        else:
            print('The Maximum number of students is 45.')
    cost_ticket = (550/n_students)+((n_students*30)/(n_students-n_students//10))
    print('The cost of Ticket per Student: $',cost_ticket)
    print('\n\n')


    name_list = {}
    while n_students>=0:
        name = input('Enter Name of Student: ')
        if name in name_list:
            print('Name already in list.')
            n_students += 1
            continue
        n_students -= 1
        paid = input('Money Paid? (y/n)')
        if paid in 'yY':
            paid = True
        else:
            paid = False
        name_list[name] = paid
        print('\n')
    print('Name\t\t|\t Paid')
    for i in name_list:
        print(i,'\t\t|\t',name_list[i])
        n_students = 0
        if name_list[i] is True:
            n_students += 1
    print('\nThe Total Number of Student: ',n_students)
    cost_ticket = (550/n_students)+((n_students*30)/(n_students-n_students//10))
    print('The Final cost of Ticket per Student: $',cost_ticket)
    print('\n\n')
    
            

if __name__ == '__main__':
    main()
