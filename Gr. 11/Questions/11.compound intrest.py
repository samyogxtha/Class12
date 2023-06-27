def n():
    print('\n\n')
n()
p = int(input('Enter your Principal Amount:'))
r = int(input('Enter Rate:'))
t = int(input('Enter Time period:'))
n()
ci = (p*(1+r/100)**t)-p
print('The compound Intrest is ',ci,'\b.')
n()