n = 5

for x in range(1, (n+5) //2 + 1):
    for y in range( (n+5) //2 - x):
        print(" ", end = "")
    for z in range( (x*2)-1 ):
        print("*", end = "")
    print()

for x in range( (n+5)// 2 + 1, n + 5):
    for y in range(x - (n+5) //2):
        print(" ", end = "")
    for z in range( (n+5 - x) *2 - 1):
        print("*", end = "")
    print()

def print_diamond_pattern(n):
    for i in range(1, n + 1):
        for j in range(n, i, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        for l in range(i - 1, 0, -1):
            print(l, end="")
        print()

    for i in range(n - 1, 0, -1):
        for j in range(n, i, -1):
            print(" ", end="")
        for k in range(1, i + 1):
            print(k, end="")
        for l in range(i - 1, 0, -1):
            print(l, end="")
        print()

n = int(input("Enter the number of rows: "))
print_diamond_pattern(n)
