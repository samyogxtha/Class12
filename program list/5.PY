'''Write a menu driven program to create a binary file and add the following information into it.
a)	Roll Number
b)	Student name
c)	Grade and Division
Also add menus to do the following:
i.	Search for a student using his roll number
ii.	Display all students in the file
iii.Modify the details of a students
iv.	Delete a student from the file'''

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
      try:
        with open('student.dat','ab') as file:
            roll = int(input('Enter Roll Number: '))
            name = input('Enter Student Name: ')
            grade = int(input('Enter Grade: '))
            div = input('Enter Division: ')
            pickle.dump([roll,name,grade,div],file)
            print('\nRecord added Succesfully')
      except:sys.stderr.write('\nERROR Try Again\n')

    elif choice == 2:
        try:
          with open ('student.dat','rb') as fl:
            dat = []
            while True:
              try:dat.append(pickle.load(fl))
              except:break
            if dat != []:
              roll = int(input("Enter the roll number of the Student: "))
              for i in dat:
                if i[0] == roll:
                  print("\nStudent Found.\n")
                  print(tabulate.tabulate([i], headers=['Roll. No.', 'Student Name', 'Grade','Division'],tablefmt='mixed_grid'))
                  break
              else:sys.stderr.write("\nStudent Not Found.\n")
            else:sys.stderr.write("File Empty\n")
        except:sys.stderr.write('File Not Found!\n')
        
    elif choice == 3:
        try:
          with open ('student.dat','rb') as fl:
            dat = []
            while True:
              try:dat.append(pickle.load(fl))
              except:break
            if dat!=[]:print(tabulate.tabulate(dat, headers=['Roll. No.', 'Student Name', 'Grade','Division'],tablefmt='mixed_grid'))       
            else:sys.stderr.write("File Empty\n")
        except:sys.stderr.write('File Not Found!\n')

    elif choice == 4:
      try:
        with open ('student.dat','rb') as fl:
          dat = []
          while True:
            try:dat.append(pickle.load(fl))
            except:break
          if dat != []:
            roll = int(input("Enter the roll number of the Student: "))
            for i in dat:
              if i[0] == roll:
                i[1] = input('Enter Student Name: ')
                i[2] = int(input('Enter Grade: '))
                i[3] = input('Enter Division: ')
                with open('student.dat','wb') as f:
                  for j in dat:
                    pickle.dump(j,f)
                  print('\nRecord Saved')
                break
            else:sys.stderr.write("\nStudent Not Found.\n")
          else:sys.stderr.write("File Empty\n")
      except:sys.stderr.write('File Not Found!\n')

    elif choice == 5:
      try:
        with open ('student.dat','rb') as fl:
          dat = []
          while True:
            try:dat.append(pickle.load(fl))
            except:break
          if dat != []:
            roll = int(input("Enter the roll number of the Student: "))
            for i in dat:
              if i[0] == roll:
                dat.remove(i)
                with open('student.dat','wb') as f:
                  for j in dat:pickle.dump(j,f)
                  print('\nRecord Deleted')
                break
            else:sys.stderr.write("\nStudent Not Found.\n")
          else:sys.stderr.write("File Empty\n")
      except:sys.stderr.write('File Not Found!\n')
    else:break