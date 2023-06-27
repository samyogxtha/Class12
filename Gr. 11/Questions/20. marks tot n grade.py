Name=input('Enter your Name:')
mt=float(input('Enter Maths Marks:'))
if mt > 80:
    print('The marks cannot be more than 80.')
    mt=float(input('Enter Maths Marks:'))
py=float(input('Enter Physics Marks:'))
if py > 70:
    print('The marks cannot be more than 70.')
    py=float(input('Enter Maths Marks:'))
ch=float(input('Enter Chemistry Marks:'))
if ch > 70:
    print('The marks cannot be more than 70.')
    ch=float(input('Enter Maths Marks:'))
cs=float(input('Enter Computer Marks:'))
if cs > 70:
    print('The marks cannot be more than 70.')
    cs=float(input('Enter Maths Marks:'))
en=float(input('Enter English Marks:'))
if en > 80:
    print('The marks cannot be more than 80.')
    en=float(input('Enter Maths Marks:'))


pmt = (mt/80)*100
ppy = (py/70)*100
pch = (ch/70)*100
pcs = (cs/70)*100
pen = (en/80)*100

per = (pmt+ppy+pch+pcs+pen)/5

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

print('Percentage =',per,'%')
print('Grade =',g)
