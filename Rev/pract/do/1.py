'''1.	a)	Write a menu-driven program in Python to:
i.	Write the following contents to a text file named “story.txt.”
“A woman finds a pot of treasure on the road while she is returning from work.
Delighted with her luck, she decides to keep it. As she is taking it home, it keeps changing.
However, her enthusiasm refuses to fade away.”
ii.	Read and display all words from the file which contains the letter 'a', 'e' and 'o' including both lowercase and uppercase.
iii.	Search for the words in the file which contains more than 6 letters and display them in reverse order.'''



def add():
    with open('story.txt','w') as file:
        content = input('\nEnter Story:')
        file.write(content)
        print('\n\t-Story-Saved-')

def disp_aeo():
    try:
        with open('story.txt') as file:
            story = file.read()
            print('Words:')
            for i in story.split():
                for j in i:
                    if j in 'aeoAEO':
                        print(i)
                        break
    except:
        print('\n\t-File-Not-Found-')
        
def search_words():
    try:
        with open('story.txt') as file:
            story = file.read()
            words = []
            for i in story.split():
                if len(i)>6:
                    words.append(i)
            print('Words:')
            words.reverse()
            for i in words:
                print(i)     
    except:
        print('\n\t-File-Not-Found-')


while True:
    print('\n\t-----MENU-DRIVEN-PROGRAM------')
    print('''1. Input Story
2. Display words containing 'a','e' and 'o'
3. Search for words containing more than 6 letters in reverse order.
0. Quit''')

    choice = int(input('\n\tEnter Choice: '))

    if choice == 1:
        add()
    elif choice == 2:
        disp_aeo()
    elif choice == 3:
        search_words()
    elif choice == 0:
        break
    else:
        print('\n\t-Enter-Valid-Choice-')
