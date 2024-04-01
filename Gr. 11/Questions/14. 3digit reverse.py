
no = int(input('Enter anlast Number:')) #365



first = no//100
other2 = no%100
second = other2//10
last = no%10
z = (last*10+second)*10+first

print(z)