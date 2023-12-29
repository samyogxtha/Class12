#1.	Write a menu driven program using functions to find:
#1.	Factorial of a number
#2.	Check the number is even or odd
#3.	Find the sum of digits of a number
#4.	Reverse the number
#5.	Check whether the number is Palindrome or not
#6.	Check the number is Amstrong or not
#(Palindrome – check the actual is same as its reverse
#Amstrong – Check the original number is same as its sum of powers of each digit raised to number of digits)

def factorial(n):
    if n==1: return 1
    else: return n*factorial(n-1)

def palindrome(n):
    r,s=0,0
    m=n
    while n>0:
        r=n%10
        s=s*10+r
        n//=10
    if m==s: return 'The number is palendrome.'
    else: return 'The number is not palendrome.'
        
def amstrong(n):
    r,s,m,count,x=0,0,n,0,n
    while n>0:
        count+=1
        n=n//10
    while m>0:
        r=m%10
        s=s+r**count
        m=m//10
    if x==s:  return 'The number is amstrong.'
    else: return 'The number is not amstrong.'
    
print('\n--------Menu-Driven-Program--------\n')
print('''1. Factorial of a number
2. Check the number is even or odd
3. Find the sum of digits of a number
4. Reverse the number
5. Check whether the number is Palindrome or not
6. Check the number is Amstrong or not
0. Quit
''')

while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')

    if choice == 1:
        n = int(input('Enter number: '))
        print(f'Factorial of the number is {factorial(n)}')
    elif choice == 2:
        n = int(input('Enter number: '))
        print(f'The number is {"Even" if n%2==0 else "Odd"}.')
    elif choice == 3:
        n = int(input('Enter number: '))
        sum=0
        for i in str(n):sum+=int(i)
        print(f'The sum of number is {sum}')
    elif choice == 4:
        n = int(input('Enter number: '))
        print(f'The reversed number is {str(n)[::-1]}')
    elif choice == 5:
        n = int(input('Enter number: '))
        print(palindrome(n))
    elif choice == 6:
        n = int(input('Enter number: '))
        print(amstrong(n))
    else:break