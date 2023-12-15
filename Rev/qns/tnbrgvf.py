import random
PICKER= 1+random.randint(0,2)
color=['blue','pink','green','red']
for i in range(1,PICKER+1):
    for j in range(i+1):print(color[j],end='')
    print()