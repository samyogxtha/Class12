print('\n\n')
n = int(input('Enter the no. of rows:'))
m = int(input('Enter the no. of coloumns:'))
print('\n\n')
l = list()
while True:
    if n != m:
        print('\n\n')
        n = int(input('Enter the no. of rows:'))
        m = int(input('Enter the no. of coloumns:'))
        print('\n\n')
        if n == m:
            break
        else:
            continue
    else:
        break






for i in range(n):
    sublist = list()
    for j in range(n):
        x = int(input('Enter number: '))
        sublist.append(x)
    l.append(sublist)



print('\n\n')



for i in range(n):
    for j in range(n):
        if i == j:
            print(l[i][j],end='\t')
        else:
            print('_',end='\t')
    print('\n\n')


print('\n\n')    


for i in range(n):
    for j in range(n):
        if (i+j) == (n-1):
            print(l[i][j],end='\t')
        else:
            print('_',end='\t')
    print('\n\n')