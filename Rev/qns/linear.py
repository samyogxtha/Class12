def lsearch(list,n):
    for i in list:
        if i == n:
            return list.index(n)
    return-1

print(lsearch([1,2,3,4,5,6],0))