def n():
    print('\n\n')
n()
x = int(input('Enter SALES: '))
c = 0
n()
if x>=50000:
    c=(x*10)/100
elif x>=30000:
    c=(x*5)/100
elif x>=15000:
    c=(x*2)/100
else:
    c=0
tot = x+c
print('Commission:',c)
n()