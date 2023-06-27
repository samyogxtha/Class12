def n():
    print('\n\n')
n()
x = int(input('Enter first Number:'))
y = int(input('Enter second Number:'))
z = int(input('Enter third Number:'))
n()
if (x>y):
    if x>z:
        print('The first Number is the Greatest.')
elif(y>x):
    if y>z:
        print('The second Number is the Greatest.')
elif z>y:
    if (z>x):    
        print('The third Number is the Greatest.')
n()