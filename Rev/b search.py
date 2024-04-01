lis=[i for i in range(10,101,10)]

def bs(lis,no):

    min,max = 0,len(lis)-1
    while min<=max:
        mid= (min+max)//2

        if lis[mid]==no:
            return mid
        elif lis[mid] < no:
            min = mid+1
        else:
            max=mid-1
    return -1

print(bs(lis,100))