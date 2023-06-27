import random,time

v = 'aeiouAEIOU'
name_list = ['Players']
no_players = int(input('\n\nEnter the number of Players: '))
score = {}
n,z = 0,1
while n < no_players:
    print('\n')
    name = input('Enter the name of Player ' + str(z) + ': ')
    if name in name_list:
        print('Name Exists\n')
    else:
        z += 1
        n += 1
        score[name] = 0
        name_list.append(name)

rounds = int(input('\nEnter Number of Rounds: '))
player = random.randint(1,no_players)
last = 'a'
for i in range(rounds):
    print('\n\n\t\tROUND',i+1,'\n')
    for j in range(no_players):
        pts = 0
        if i == 0 and j == 0:
            print('Player | ',name_list[player],'\n2')
            word = input('Enter Word: ')
            for k in word:
                if k in v:
                    score[name_list[player]] += 10
                    pts += 10
                else:
                    score[name_list[player]] += 5
                    pts += 5
            print('\t\t\t\t\t+',pts,'Points')
            last = word[-1]
        else:
            print('\nPlayer | ',name_list[player],'\nLast Letter: \'',last,'\'\n')
            word = input('Enter Word: ')
            if word.startswith(last):
                for j in word:
                    if j in v:
                        score[name_list[player]] += 10
                        pts += 10
                    else:
                        score[name_list[player]] += 5
                        pts += 5
                print('\t\t\t\t\t+',pts,'Points')
            else:
                print('The word does not start with \'',last,'\'. \n\t\t\t\t\t-10 Points')
                score[name_list[player]] -= 10
                pts -= 10
            last = word[-1]
        if player == no_players:
            player = 1
        else:
            player += 1

print('\n\n\t\tGAME OVER!')
#Score
'''
high,low = score[name_list[1]],score[name_list[1]]
win,lose= name_list[1],name_list[1]
for i in name_list[2:len(name_list)]:
    if score[i] > high:
        high = score[i]
        win = i
    if score[i] < low:
        low = score[i]
        lose = i
print('\n\nWinner: ',win,'\tPoints = ',high)
print('\nLoser: ',lose,'\tPoints = ',low)
'''

#Score v2
print('\n\n\t\t  SCORE\n\tPlayer\t\t\tScore\n')
for i in score:
    print('\t',i,'\t\t\t',score[i])


time.sleep(8)