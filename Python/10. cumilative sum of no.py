l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    l.append(int(input('Enter the element: ')))
cs = 0
l2 = []
for i in l:
    cs += i
    l2.append(cs)
print(l2)
