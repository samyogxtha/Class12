'''Write a program to generate random numbers between two limits. '''

import random

ll = int(input('Enter Lower limit: '))
ul = int(input('Enter Upper limit: '))

n = int(input('How many numbers? '))

for i in range(n):print(random.randint(ll,ul))