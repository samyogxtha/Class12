import random

def n():
    print('\n\n')
n()
rounds = int(input('Enter the number of Rounds:'))
user_pts,comp_pts = 0,0
n()
for i in range(1,rounds+1):
    user_int = input('Enter Rock(1), Paper(2), and Scissors(3).')
    moji = 0
    if user_int == 1:
        moji = '🤛🏻'
    elif user_int == 2:
        moji = '📄'
    else:
        moji = '✂'
    comp_int = random.randint(1,3)
    moji2 = 0
    if comp_int == 1:
        moji2 = '🤛🏻'
    elif comp_int == 2:
        moji2 = '📄'
    else:
        moji2 = '✂'
    if user_int == 1:
        print('Computer Chooses: ',comp_int,moji2)
        print('Your Choice: ',comp_int,moji)
        if comp_int == 1:
            print('DRAW\n')
        elif comp_int == 2:
            print('You LOSE\n')
            comp_pts += 1
        else:
            print('You WIN\n')
            user_pts += 1
    elif user_int == 2:
        print('Computer Chooses: ',comp_int,moji2)
        print('Your Choice: ',comp_int,moji)
        if comp_int == 2:
            print('DRAW\n')
        elif comp_int == 3:
            print('You LOSE\n')
            comp_pts += 1
        else:
            print('You WIN\n')
            user_pts += 1
    else:
        print('Computer Chooses: ',comp_int,moji2)
        print('Your Choice: ',comp_int,moji)
        if comp_int == 3:
            print('DRAW\n')
        elif comp_int == 2:
            print('You LOSE\n')
            comp_pts += 1
        else:
            print('You WIN\n')
            user_pts += 1
n()
print('FINAL score:',user_pts,comp_pts)
print('Final RESULTS',end=' ')
if user_pts == comp_pts:
    print('DRAW')
elif user_pts>comp_pts:
    print('You WIN!!')
else:
    print('YouLOSE')
n()