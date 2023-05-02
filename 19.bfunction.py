def bfunction(list,chk_no):
    for i in len(list):
        if i == chk_no:
            index = list.index(i)
    
    return index

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