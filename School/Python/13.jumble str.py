def jumble(str):
    jumbled_str = ''
    for i in str:
        if i.isupper():
            jumbled_str += i.lower()
        elif i.islower():
            jumbled_str += i.upper()
        elif i.isnum():
            jumbled_str += '*'
        else:
            jumbled_str += '@'
    return jumbled_str

string = input('Enter String: ')
print('The Jumbled String is: ',jumble(string))