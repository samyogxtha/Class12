import pickle
from tkinter import W

from numpy import double

def copyData():
    with open('story.dat','rb') as file:
        lis=[]
        while True:
            try:
                lis.append(pickle.load(file))
            except:
                break
    
    with open('basket.dat','ab') as file2:
        count=0
        for i in lis:
            if i[0] == 'Basket Ball':
                pickle.dump(i,file2)
                count+=1

    return count


a = {1:['aaa','aaaa'],2:['bbb','bbbb']}

def findType(mtype):
    
    with open('cinema.dat','rb') as file:
        cont = pickle.load(file)

        for i in cont:
            if cont[i][1] == mtype:
                print(i,cont[i])

findType('bbbb')


#----------------------------------------------------------------
import mysql.connector as ms

con = ms.connect(user='root',host='localhost',passwd='tiger',database='school')

cur = con.cursor()

rno = int(input('Enter rno: '))
name = input('Enter Name: ')
dob = input('Enter Dob: ')
fee = int(input('Enter Fee: '))

cur.execute(f'insert into students values({rno},"{name}","{dob}",{fee})')
con.commit()

cur.close()


#----------------------------------------------------------------
import mysql.connector

con = mysql.connector.connect(host='localhost',user='root',passwd='tiger',database = 'school')
cur=con.cursor()

cur.execute(f'select * from students where fee>5000')
cont = cur.fetchall()
for i in cont:
    print(i)

cur.close()
con.close()

#----------------------------------------------------------------
travel = []
def push_element(nlist):
    for i in nlist:
        if i[1]!='india' and i[2]<35000:
            travel.append(i[:2])

def pop_element():
    while True:
        try:
            print(travel.pop())
        except:
            print('Stack Empty')