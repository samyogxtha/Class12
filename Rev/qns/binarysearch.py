def bsearch(list,n):
    min,max=0,len(list)-1
    while max>=min:
        mid=(min+max)//2
        if list[mid] == n:return mid
        elif list[mid] > n:max=mid-1
        else:min=mid+1
    return -1
    






print(bsearch([1,2,3,4,5,6],6))