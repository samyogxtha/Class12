'''Write a menu-driven program in Python to: 

Write the following contents to a text file named “story.txt.” 

“A woman finds a pot of treasure on the road while she is returning from work. 

Delighted with her luck, she decides to keep it. As she is taking it home, it keeps changing. 

However, her enthusiasm refuses to fade away.” 

Read and display all words from the file which contains the letter ‘a,’ ‘e’ and ‘o’ including both lowercase and uppercase. 

Search for the words in the file which contains more than 6 letters and display them in reverse order.'''

def story():
    with open('story.txt','w') as f:
        story = input('enter story to input:\n')
        f.write(story)

def aeo_Display():
    with open('story.txt') as f:
        story = f.read()
        words = story.split()
        for i in words:
            for j in i:
                if j in 'aeoAEO':
                    print(i)
                    break

def Len_Display():
    with open('story.txt') as f:
        story = f.read()
        words = story.split()
        sixwords=[]
        for i in words:
            if len(i)>6:
                sixwords.insert(-1,i)
        for i in sixwords:
            print(i)

while True:
    print('''------------MENU-DRIVEN-PROGRAMME------------
    1. Write Story into file.
    2. Display all words with \'a\',\'e\' and \'o\' including uppercase and lowercase
    3. Display words with more than 6 characters in reverse order
    0. Exit''')
    ch = input('enter choice: ')
    if ch == '1':story()
    elif ch == '2':aeo_Display()
    elif ch == '3':Len_Display()
    elif ch == '0':break
    else:print('Please insert a valid choice')
