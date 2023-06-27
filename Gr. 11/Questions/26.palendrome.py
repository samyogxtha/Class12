n =int(input('Enter any number: '))
r,s=0,0
m=n
while n>0:
    r=n%10
    s=s*10+r
    n=n//10
if m==s:
    print('The sum of number is palendrome.')
else:
    print('The sum of number is not palendrome.')