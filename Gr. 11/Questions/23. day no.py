def n():
    print('\n\n')
n()
no = float(input('Enter DAY Number: '))
n()
ref = no%7
if ref == 1:
    print('Sunday')
elif ref == 2:
    print('Monday')
elif ref == 3:
    print('Tuesday')
elif ref == 4:
    print('Wednesday')
elif ref == 5:
    print('Thrusday')
elif ref == 6:
    print('Friday')
else:
    print('Saturday')
n()