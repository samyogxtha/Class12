l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    x = int(input('Enter the element: '))
    if x in l:
        q+=1
        continue
    else:
        l.append(x)
s = 0
for i in l:
    if i%2==0:
        s+=i**2
print('Sum: ',s)