def lsearch(list,chk_no):
    for i in list:
        if i == chk_no:
            return list.index(i)
    else:
        return -1

def main():
    list = []
    n_list = int(input('Enter the number of elements in List: '))
    for i in range(n_list):
        list.append(int(input('Enter Number: ')))
    number = int(input('Enter Number to Search: '))
    index_of_number = lsearch(list,number)
    if index_of_number == -1:
        print('The Number is not in List.')
    else:
        print('The index of Number in List is: ',index_of_number)

if __name__ == '__main__':
    main()