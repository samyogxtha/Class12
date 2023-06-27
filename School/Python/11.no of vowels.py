def vowels_counter(string):
    count = 0
    for i in string:
        if i in 'aeiouAEIOU':
            count += 1
    return count

string = input('Enter String: ')
print('The number of vowels in the String is: ',vowels_counter(string))