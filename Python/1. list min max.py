def min(x):
    min = x[0]
    for i in x:
        if min > i:
            min = i
    return min

def max(x):
    max = x[0]
    for i in x:
        if max < i:
            max = i
    return max

l = []
q = int(input('Enter the no of elements in the list: '))
for i in range(q):
    x = int(input('Enter the element: '))
    l.append(x)
print("\vThe maximum value: ", max(l))
print("The minimum value: ", min(l))