'''Write a menu driven program to manipulate a text file. Add the following options: 
i.   Input some contents into a file.
ii.  Output the contents from the file.
iii. Count and display number of vowels, consonants, lowercase and uppercase characters in the file.'''

print('\n\t ----------Text-File-Manipulation----------')
print('\n1. Input some contents into the file\n2. Output the contents from the file\n3. Count and display number of vowels, consonants, lowercase and uppercase characters in the file.')

while True:
    ch=int(input('\nEnter your choice (0. to exit): '))
    if ch==1:
        with open('file.txt','w') as f:
            n = input('\nEnter text: ')
            f.write(n)
            print('Input Saved')
    elif ch==2:
        with open('file.txt') as f:print(f'\nContents:\n\n{f.read()}')
    elif ch==3:
        with open('file.txt') as f:
            v,c,l,u=0,0,0,0
            for i in f.read():
                if i.isalpha():
                    if i.lower() in 'aeiou':v+=1
                    if i.lower() in 'bcdfghjklmnpqrstuvwxyz':c+=1
                    if i.islower():l+=1
                    if i.isupper():u+=1
            print(f'\nNumber of Vowels: {v}\nNumber of consonants: {c}\nNumber of lowercase characters: {l}\nNumber of uppercase characters: {u}')
    else:break