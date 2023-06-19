l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    l.append(int(input('Enter the element: ')))
t = int(input('Enter Target Value: '))

got = False
tup = ()
for i in l:
    if got == True:
        break
    for j in l:
        if i+j == t:
            tup = (l.index(i),l.index(j))
            got = True
            break
if got == True:
    print('Index = ',tup)
else:
    print('No elements add up to the target Value.')