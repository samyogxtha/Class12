import random
pick=random.randint(3,3)
city=["DELHI " , "MUMBAI " , "CHENNAI " , "KOLKATA"]
for i in city:
    for j in range(1, pick):
        print(i, end=" " )
    print()