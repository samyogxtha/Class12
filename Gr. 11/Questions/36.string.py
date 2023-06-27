print('\n\n')
s = input('Enter sentence: ')
vo,co,sp = 0,0,0
v = 'aeiouAEIOU'
c = 'bcdfghjklmnpqrstvwxyzBCDEGHJKLMNPQRSTVWXYZ'

for i in s:
    if i in v:
        vo += 1
    elif i in c:
        co += 1
    elif i == ' ':
        sp += 1
print('Number of Characters:   ',len(s)-sp)
print('Number of Vowels: \t',vo)
print('Number of Consonants:   ',co)
print('Number of Words: \t',sp+1)
print('\n\n')