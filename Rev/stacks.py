inventory=[[1,'bla',200,100],[2,'wll',200,800]]
items=[]

def push(inventory):
    for i in inventory:
        if i[3]>100:
            items.append(i)

def pop():
    while True:
        try:print(items.pop())
        except:print('Stack Empty')
