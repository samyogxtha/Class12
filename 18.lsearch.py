def lsearch(list,chk_no):
    for i in list:
        if i == chk_no:
            index = list.index(i)
            break
    else:
        index = 'Not Found'
    return index

def main():
    list = []
    n_list = int(input('Enter the number of elements in List: '))
    for i in range(n_list):
        list.append(int(input('Enter Number: ')))
    number = int(input('Enter Number to Search: '))
    index_of_number = lsearch(list,number)
    print('The index of Number in List is: ',index_of_number)

if __name__ == '__main__':
    main()