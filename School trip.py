def main():
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
    for i in range(n_students):
        name = input('Enter Name of Student: ')
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
    
            

if __name__ == '__main__':
    main()
