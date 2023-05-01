def main():
    while True:
        n_students = int(input('Enter the number of Students: '))
        if 0 <= n_students <= 45:
            break
        else:
            print('The Maximum number of students is 45.')
    cost_ticket = (550/n_students)+((n_students*30)/(n_students-n_students//10))
    print('The cost of Ticket per Student: $',cost_ticket)


    name_list = {}
    for i in range(n_students)


if __name__ == '__main__':
    main()
