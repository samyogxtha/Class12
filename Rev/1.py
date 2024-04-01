from math import *
from random import *

lis = [0,1,2,3,4,5,6,7,8,9]

def ar(x,n=2):
    
    for i in range(n):
        x.insert(0,x.pop())
    
    return x

print(ar(x=lis))
print(lis)

def factoral(n):
    if n!=1:
        return n*factoral(n-1)
    else:
        return n
print(factoral(5))



#name='Vikrant'
#print(name.replace('nt','m').upper())


'''for i in range(1,0,-1):
    print(randrange(30,10,-3))



print([i for i in range(1,0,-1)])

x=5
def func1():
    x=2
    x=x+1
def func2():
    global x
    x=x+1
print(x)
func1()
print(x)
func2()
print(x)'''



'''a= 1,2,3

i=0
while i<len(a):
    print(a[i])
    i+=1'''


#print(f'{a}\n{b}\n{c}',end='d\n')
#print(ceil(22.5))