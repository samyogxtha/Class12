lis = [1,2,3,4,5,6,7,21]
prime = []

for i in lis:
    if i > 1:
        for j in range(2,(i//2)+1):
            if (i % j) == 0:
                break
        else:
            prime.append(i)
        

print(prime)
