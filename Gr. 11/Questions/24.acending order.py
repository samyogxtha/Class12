x = int(input("Enter first number: "))
y = int(input("Enter second number: "))
z = int(input("Enter third number: "))
min,mid,max=0,0,0
if y>=x<=z:
    if y<=z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
elif x>=y<=z:
    if x<=z:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
elif x>=z<=y:
    if x<=y:
        min,mid,max=x,y,z
    else:
        min,mid,max=x,z,y
print("Numbers in ascending order = ",min,mid,max)