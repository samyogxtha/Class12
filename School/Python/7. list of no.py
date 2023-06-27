l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    x = int(input('Enter the element: '))
    if x in l:
        q+=1
        continue
    else:
        l.append(x)