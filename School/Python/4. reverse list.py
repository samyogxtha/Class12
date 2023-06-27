l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    l.append(int(input('Enter the element: ')))
r = []
for i in l:
    r.insert(0,i)
print(r)