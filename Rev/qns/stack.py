#Write a program to implement a stack. for this book details.(booknumber,bookname).Each item Node of the stack.contains two type of information.Book number and its name.Just implement display andpush operation.

def isempty(s):
    if len(s)==0:return True
    else:return False

def push(s,item):
    s.append(item)
    top=len(s)-1

def display(s):
    if isempty(s):print('Empty')
    else:
        top = len(s)-1
        for i in range(top,-1,-1):
            print(s[i])


s=[2,3,4]
top=None

while True:
    print('1.add a book\n2.display\n3.quit')
    break

display(s)

def dum():
    return 10,20,30
a=dum()

print(a,len(a))