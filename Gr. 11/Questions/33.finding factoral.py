n = int(input('Enter any number: '))
for i in range(1,n+1):
    s=1
    for j in range(1,i+1):
        s=s*j
    print(i,'\b! = ',s)