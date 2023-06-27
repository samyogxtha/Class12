def n():
    print('\n\n')
n()
BS = int(input('Enter BASIC SALARY: '))
DA = int(input('Enter DA: '))
TA = int(input('Enter TA: '))
HRA = int(input('Enter HRA: '))
n()
aa=0
g = input('Are you a Girl? (y/n)')
sk = input('Skilled Employee? (y/n)')
n()
if (g=='y') or (g=='Y'):
    aa += (BS*5)/100
if (sk=='y') or (sk=='Y'):
    aa += (BS*10)/100
tot = BS+DA+TA+HRA+aa
print('Total Salary:',tot)
n()