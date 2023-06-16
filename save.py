import random
PICK=random.randint(0, 3)
CITY=["DELHI", "MUMBAI", "CHENNAI", "KOLKATA"]
for i in CITY:
    for j in range (1, PICK):
        print(i, end="")
    print()
