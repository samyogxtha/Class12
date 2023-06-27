def n():
    print('\n\n')
n()
a = int(input('Enter Side 1: '))
b = int(input('Enter Side 2: '))
c = int(input('Enter Side 3: '))
n()
s = (a+b+c)/2
ar = (s*(s-a)*(s-b)*(s-c))**(1/2)
ar2 = '{:.2f}'.format(ar)
print('The Area of the Triangle is',ar2,'\b.')
n()