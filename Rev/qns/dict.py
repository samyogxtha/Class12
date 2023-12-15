def freq(lis,d):
    for i in lis:
        if i not in d:
            d[i]=1
        else:d[i]+=1
    return d


lis=[10, 10, 20, 30, 90, 50, 60, 70, 90, 90, 100]

print(freq(lis,d={}))