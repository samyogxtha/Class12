def same_elements(l1,l2):
    l = list()
    for i in l1:
        if i in l2:
            if i not in l:
                l.append(i)
    return l

list1 = list()
n_list1 = int(input('Enter the number of elements in List 1: '))
for i in range(n_list1):
    list1.append(int(input('Enter Number: ')))

list2 = list()
n_list2 = int(input('Enter the number of elements in List 1: '))
for i in range(n_list2):
    list2.append(int(input('Enter Number: ')))
    
print('The same elements in both lists are: ',same_elements(list1,list2))