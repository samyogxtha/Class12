def bfunction(list,chk_no):
    list.sort()
    min = 0
    max = len(list) - 1
    mid = (min + max) // 2

    while min <= max:
        if list[mid] == chk_no:
            return mid
        elif list[mid] < chk_no:
            max = mid + 1
        else:
            max = mid - 1
    return 'Not Found'

def main():
    list = []
    n_list = int(input('Enter the number of elements in List: '))
    for i in range(n_list):
        list.append(int(input('Enter Number: ')))
    number = int(input('Enter Number to Search: '))
    index_of_number = bfunction(list,number)
    print('The index of Number in List is: ',index_of_number)

if __name__ == '__main__':
    main()