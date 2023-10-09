def prime_nos(list):
    primes = []
    for i in list:
        if i > 1:
            for j in (2,(i//2)+1):
                if i%j == 0:
                    break
            else:
                primes.append(i)
    return primes

list = list()
n_list = int(input('Enter the number of elements in List: '))
for i in range(n_list):
    list.append(int(input('Enter Number: ')))

print('Prime number in the list are: ',prime_nos(list))