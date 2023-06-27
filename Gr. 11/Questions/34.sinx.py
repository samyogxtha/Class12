#Write a program to compute sinx for given x. The user should supply x and a positive integer n. We compute the sine of x using the series and the computation should use all terms in the series up through the term involving xn

#sin x = x - x3/3! + x5/5! - x7/7! + x9/9! ........

x = int(input('Enter x: '))
n = int(input('Enter n: '))
s,f,a = 0,0,0

for i in range(1,n+1):
    while a>=n:
        a = 2*i-1
f = 1
for j in range(1,a+1):
    f*=j
print(a,f)
if a%2==0:
    s += (x**a)/f
else:
    s -= (x**a)/f
print('sin ',x,'= ',s)