l = list()
marks = list()
sum=0

for i in range(5):
    m = int(input('Enter subject '+str(i+1)+' marks: '))
    marks.append(m)
print('The MARKS entered are:',marks)
for j in marks:
    sum += j
per = sum/5
print('Total=',sum)
print('Percentage=',per,'%')

if per>=91:
    g='A1'
elif per>=81:
    g='A2'
elif per>=71:
    g='B1'
elif per>=61:
    g='B2'
elif per>=51:
    g='C1'
elif per>=41:
    g='C2'
elif per>=33:
    g='D'
else:
    g='E'

print('GRADE=',g)