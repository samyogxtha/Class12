'''Write a program to input a tuple of numbers and check number of times a particular number appears in that tuple. If the number, you are searching is not in the tuple then output the message “Sorry, the number you are searching is not in the tuple”.'''

k = eval(input('\nEnter tuple: '))
n = int(input('Enter Number to check: '))

count=0
for i in k:
    if i == n:count+=1
if count!=0:print(f'\nCount of {n} in the tuple: {count}\n')
else:print('\nSorry, the number you are searching is not in the tuple\n')