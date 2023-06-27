ll = int(input('Enter Lower Limit: '))
ul = int(input('Enter Upper Limit: '))
od,ev = 0,0
if ll/2==0:
    for i in range(ll,ul,2):
        ev += i
if ll/2==1:
    for i in range(ll+1,ul,2):
        od += i
print('Sum of Odds: ',od)
print('Sum of Even: ',ev)