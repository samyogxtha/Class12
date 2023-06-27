def n():
    print('\n\n')
n()
bm = float(input('Enter Bill Amount: '))
n()
print('Credit Card\t(c)\nDebit Card\t(d)\nNet Banking\t(n)\nCash\t\t(x)')
n()
pm = input('Select Payment Methord: ')
n()
dc = 0
if pm == 'c':
    dc=(bm*10)/100
elif pm == 'd':
    dc=(bm*5)/100
elif pm == 'n':
    dc=(bm*2)/100
else:
    dc=0

tot = bm-dc

a = str(tot)
val = a.split('.')[1]
val = int(val)

def xy():
    if val == 0:
        #tot2 = int(tot)
        print(int(tot))
    else:
        tot3 = "{:.2f}".format(tot)
        print(tot3)

if dc == 0:
    print('Net payable Amount:')
    xy()
else:
    print('Discount:',dc)
    print('Net payable Amount:')
    xy()
n()