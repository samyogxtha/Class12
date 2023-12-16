'''Write a menu driven program using dictionary for the following:
i. Create a dictionary with a character as key and a word starting with that letter as value.
ii. Display all key value pairs in the dictionary.
iii. Search for a particular dictionary and print its value.
iv. Modify the value of a particular key.
v. Delete a key value pair from the dictionary'''

print('\n--------Menu-Driven-Program--------\n')
print('''1. Create a dictionary
2. Display all key value pairs in the dictionary
3. Search for a particular dictionary and print its value
4. Modify the value of a particular key
5. Delete a key value pair from the dictionary
0. Quit
''')

d = {}
while True:
    choice = int(input('\n\tEnter choice: '))
    print('\n')
    if choice == 1:
        n = input('Enter Sentence: ')
        
        for i in n.split():
            if i[0].lower() not in d:d[i[0].lower()]=[i]
            else:
                a=d.get(i[0].lower())
                a.append(i)
                print(a)
                d[i[0].lower()]=a
    
    elif choice == 2:
        print('\nDictionary: ')
        print(d,'\n')
    elif choice == 3:
        for i in d:
            print(d.values())

