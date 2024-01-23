'''a)	Write a menu-driven program in Python to:
i.	Write the following contents to a text file named “story.txt.”
“A woman finds a pot of treasure on the road while she is returning from work.
Delighted with her luck, she decides to keep it. As she is taking it home, it keeps changing.
However, her enthusiasm refuses to fade away.”
ii.	Read and display all words from the file which starts with the letter ‘p,’ ‘t’ and ‘r’ including both uppercase and lowercase.
iii.	Search for the word ‘treasure’ in the file and display how many times the word appears in the file. Display the message “Word not found” if the word is not existing in the file.'''

def story():
    with open('story.txt','w') as f:
        story = input('\nEnter story to input: ')
        f.write(story)

def ptr_disp():
    with open('story.txt') as f:
        story = f.read()
        words = []
        for i in story.split():
            if i[0] in 'ptrPTR':
                words.append(i)
        if words==[]:
            print('No Words found')
        else:
            print('Words:')
            for i in words:
                print(i)

def treasure_find():
    with open('story.txt') as f:
        story = f.read()
        tcount=0
        for i in story.split():
            if i.lower() == 'treasure':
                tcount+=1
        if tcount!=0:
            print(f'\nCount of the word "treasure": {tcount}')
        else:
            print('\nWord not found')

while True:
    print('''\n\n------------MENU-DRIVEN-PROGRAMME------------
    1. Write Story into file.
    2. Display all words with 'p','t' and 'r' including uppercase and lowercase
    3. Search and display the count of the word 'treasure'
    0. Exit''')
    ch = input('\n\tEnter choice: ')
    if ch == '1':story()
    elif ch == '2':ptr_disp()
    elif ch == '3':treasure_find()
    elif ch == '0':break
    else:print('Please insert a valid choice')
