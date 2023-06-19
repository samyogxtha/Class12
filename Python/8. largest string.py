l = []
q = int(input('Enter the no of elements in the list: '))
n = 0
while n < q:
    x = input('Enter String ')
    if x in l:
        print('The string is already in the list')
    else:
        n += 1
        l.append(x)

long = 0
longest = l[0]
for i in l:
    if len(i) > long:
        long = len(i)
        longest = i
print(longest)