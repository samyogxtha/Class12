l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    x = int(input('Enter the element: '))
    if x in l:
        q+=1
        continue
    else:
        l.append(x)

p = []
for i in l:
    for j in (2,(i//2)+1):
        if i%j == 0:
            break
    else:
        p.append(i)
print(p)