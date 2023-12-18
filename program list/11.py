'''Write a program to implement stack in Python using list. Include functions to push, pop, display and show peek value.'''

def isempty(s):
    if len(s)==0:return True
    else:return False

def push(s,item):
    global top
    s.append(item)
    top=len(s)-1

def pop(s):
    global top
    if isempty(s):print('Stack Empty')
    else:
        s.pop()
        top = len(s)-1

def display(s):
    global top
    if isempty(s):print('Stack Empty')
    else:
        top = len(s)-1
        print('Stack:')
        for i in range(top,-1,-1):
            print(s[i])

def peek(s):
    global top
    if isempty(s):print('Stack Empty')
    else:return s[top]

print('''\n----------STACK-IMPLEMENTATION----------
1. Push
2. Pop
3. Display All
4. Peek
Press any other kay to Quit''')

s = []
top = None

while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')
    if choice == 1:
        push(s,input('Enter item to Push: '))
        print('Item Pushed')
    elif choice == 2:
        pop(s)
        print('Item Popped')
    elif choice == 3:display(s)
    elif choice == 4:print(f'Peek Value: {peek(s)}')
    else:break