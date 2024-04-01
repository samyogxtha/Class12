travel = []
def push_element(nlist):
    for i in nlist:
        if i==9:
            travel.append(list(i[0:1]))

dl =[[1,2,3,4,5,6,7,8,9,10],[10,20,30,40,50,60,70,80,90,100]]

print(list(dl[0][:3]))

push_element(dl)
print(travel)
