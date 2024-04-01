


s =[i for i in range(10,101,10)]
top=9

def isempty(s):
    if len(s)==0:return True
    return False

def push(s,item):
    global top
    s.append(item)
    top=len(s)-1

def pop(s):
    global top
    if isempty(s):return 'Underflow'
    popitem = s.pop()
    if len(s)==0:top=None
    else: top = len(s)-1
    return popitem

def peek(s):
    global top
    if isempty(s):return 'Underflow'
    return s[top]

def size(s):
    if isempty(s):return 'Underflow'
    return top+1

def show(s):
    for i in range(top,-1,-1):
        print(s[i],'==> ',end='')


show(s)