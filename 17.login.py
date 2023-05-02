login_details = {'Samyog':'samyog123','Idris':'idris123','Hussain':'hussain123'}

def signup():
    while True:
        username = input('Enter username: ')
        if username in login_details:
            print('The user already Exists.')
            continue
        password = input('Enter password: ')
        login_details[username] = password
        break

def login():
    while True:
        username = input('Enter username: ')
        if username not in login_details:
            print('User not Found.')
            continue
        password = input('Enter password: ')
        if login_details[username] == password:
            print('Log In Successful!')
        else:
            print('Invalid Password')
        break

def main():
    while True:
        print('1. Sign up\n2. Log In')
        qn = int(input('Enter Choice: '))
        if qn == 1:
            signup()
        else:
            login()

if __name__ == '__main__':
    main()