def cost_check(n_students):
    cost_coach = 550 / n_students
    n_disc = n_students // 10
    cost_each = ((n_students - n_disc) * 30)/n_students
    cost_total = "{:.2f}".format(cost_coach + cost_each)
    return cost_total

def main():
    print('\n\n')
    while True:
        n_students = int(input('Enter the number of Students: '))
        if 0 <= n_students <= 45:
            break
        else:
            print('The Maximum number of students is 45.')
    cost_ticket = cost_check(n_students)
    print('The cost of Ticket per Student: $',cost_ticket)
    print('\n\n')
    name_list = {}
    n_count = 0
    while n_students>0:
        name = input('Enter Name of Student: ')
        if name in name_list:
            print('Name already in list.')
            continue
        n_students -= 1
        paid = input('Money Paid? (y/n)')
        if paid in 'yY':
            paid = True
            n_count += 1
        else:
            paid = False
        name_list[name] = paid
        print('\n')
    print('Sl  Name\t\tPaid')
    sl_no = 1
    for i in name_list:
        print(sl_no,'  ',i,'\t\t',name_list[i])
        sl_no += 1
    print('\nThe Final Number of Student Going: ',n_count)
    cost_ticket = cost_check(n_count)
    print('The Final cost of Ticket per Student: $',cost_ticket)
    print('\n\n')

if __name__ == '__main__':
    main()