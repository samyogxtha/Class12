def factoral(n):
    if n==1:return 1
    else:return n*factoral(n-1)

def primeno(n):
    if n<=1:return False
    for i in range(2,(n//2)+1):
        if n%i == 0:return False
    return True

#print(primeno(-5))

import pickle,tabulate,sys

print('\n--------Menu-Driven-Program--------\n')
print('''1. Enter Student Details 
2. Search for a student using his roll number
3. Display all students in the file
4. Modify the details of a students
5. Delete a student from the file
0. Quit
''')

while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')

    if choice == 1:
        with open('file.bat','ab') as f:
            
            pickle.dump([int(input('roll:')),input('name:'),int(input('grade:'))],f)
            print('nhbgvfcd')
    elif choice==2:
        with open ('file.bat') as f:
            try:
                while True:
                    pickle.load(f)
