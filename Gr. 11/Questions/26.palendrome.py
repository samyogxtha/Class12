n =int(input('Enter any number: '))
r,s=0,0
m=n
while n>0:
    r=n%10
    s=s*10+r
    n//=10
    print(r,s,n)
if m==s:
    print(s)
else:
    print(s)


