def character_counter(str,char):
    count = 0
    for i in str:
        if i == char:
            count += 1
    return count

string = input('Enter String: ')
character = input('Enter Character to check: ')
print('The number of Character in the String is: ',character_counter(string,character))