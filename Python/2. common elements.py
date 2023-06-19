n = int(input('Number of elements in list 1: '))
m = int(input('Number of elements in list 2: '))
l = []
l1 = []
l2 = []

for i in range(n):
    l1.append(int(input('Enter Number in list 1: ')))
for i in range(m):
    l2.append(int(input('Enter Numberin list 2: ')))

for i in l1:
    if i in l2:
        l.append(i)
print(l)