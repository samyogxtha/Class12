n =int(input('Enter any number: '))
r,s,m,count,x=0,0,n,0,n
while n>0:
    count+=1
    n=n//10
while m>0:
    r=m%10
    s=s+r**count
    m=m//10
if x==s:
    print('The number is amstrog.')
else:
    print('The number is not amstrog.')