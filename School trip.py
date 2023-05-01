def main():


    cost_coach = 550
    cost_ticket = 30
    while True:
        n_students = int(input('Enter the number of Students: '))
        if 0 <= n_students <= 45:
            break
        else:
            print('The Maximum number of students is 45.')

if __name__ == '__main__':
    main()
