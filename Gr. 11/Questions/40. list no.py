n = int(input('How many numbers?'))
l = list()
for i in range(n):               
    x = int(input('Enter NUMBER at position'+str(i+1)+': '))
    l.append(x)
print('List of Numbers is ',l)