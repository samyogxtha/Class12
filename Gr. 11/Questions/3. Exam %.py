#WAP to enter Name, marks of 5 subject and calculate total & percentage of student.

Name = input('Enter your Name:')
m=int(input('Enter Maths Marks:'))
p=int(input('Enter Physics Marks:'))
c=int(input('Enter Chemistry Marks:'))
cs=int(input('Enter Computer Marks:'))
e=int(input('Enter English Marks:'))

tot=m+p+c+cs+e
print('Total Marks:',tot)

print('\n\n')

per=tot/5
per2="{:.2f}".format(per)
print('You got ',per2,'%.')
print('\n\n')