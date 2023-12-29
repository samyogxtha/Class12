#Write a program to input a sentence and a word, and check whether the word exists in the sentence or not. If yes, find the number of occurrences of the word in the sentence.

string = input('\nEnter Sentence: ')
word = input('Enter Word: ')

w_count=0
for i in string.split():
    if i == word: w_count+=1
if w_count==0:print('\nWord not Found')
else:print(f'\nWord Found \nWord Count: {w_count}')