#2.	Write a program using functions to input a list of numbers and find:
#   i.   Sum of elements in the list
#   ii.  Sum of elements at odd positions
#   iii. Sum of elements at even positions

n = int(input('\nNumber of elemements in the list: '))
lis = []
for i in range(n):lis.append(int(input('Enter Number: ')))

s_odd,s_even = 0,0
for num in lis:
    if num%2==0:s_even += num
    else:s_odd += num
print('\nSum of Numberss: ',s_odd+s_even)  
print('Sum of Odds: ',s_odd)
print('Sum of Even: ',s_even)