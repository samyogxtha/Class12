n = int(input('Enter any Number: '))
f = 0
s = 1
print(f,s,end=' ')
for i in range(2,n):
    a = f+s
    print(a,end=' ')
    f = s
    s = a
