l=[i for i in range(1,11)]

def modifylist(l,n):

    for i in range(len(l)):
        if l[i]%n==0:
            l[i]+=5
        else:
            l[i] -= 5
    print(l)

modifylist(l,5)