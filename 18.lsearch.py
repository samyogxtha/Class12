def lsearch(list,chk_no):
    index = -1
    for i in list:
        index += 1
        if i == chk_no:
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