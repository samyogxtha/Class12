ch = 'y'
sum,s,l = 0,0,0
while ch == 'y':
    n = int(input('enter ;'))
    sum += n
    if n>l:
        l=n
    else:
        s=n
    ch=input('y/n')
print(sum)
print(s)
print(l)