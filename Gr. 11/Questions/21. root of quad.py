import math

a = int(input('Enter a: '))
b = int(input('Enter b: '))
c = int(input('Enter c: '))
if a==0:
    print('a cannot be ZERO')
    a = int(input('Enter a: '))
D = b**2-4*a*c
if D==0:
    print('The Roots are Real and Equal.')
    r = -b/2*a
    print('Root:',int(r))
elif D>0:
    print('The Roots are Real and Distinct.')
    r1 = (-b+math.sqrt(D))/2*a
    r2 = (-b-math.sqrt(D))/2*a
    print('Roots:',r1,',',r2)
else:
    print('The Roots are Imaginary.')