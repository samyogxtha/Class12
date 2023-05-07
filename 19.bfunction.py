def bfunction(list,chk_no):
    list.sort()
    min,max = 0,len(list) - 1
    while min <= max:
        mid = (min + max) // 2
        if list[mid] == chk_no:
            return mid
        elif list[mid] < chk_no:
            min = mid + 1
        else:
            max = mid - 1
    return -1

def main():
    list = []
    n_list = int(input('Enter the number of elements in List: '))
    for i in range(n_list):
        list.append(int(input('Enter Number: ')))
    print('\nList: ',list)
    number = int(input('Enter Number to Search: '))
    index_of_number = bfunction(list,number)
    if index_of_number == -1:
        print('The Number is not in List.')
    else:
        print('The index of Number in List is: ',index_of_number)

if __name__ == '__main__':
    main()