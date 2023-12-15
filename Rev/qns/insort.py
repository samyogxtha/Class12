import bisect # import module

a = [2, 4, 6, 8, 10, 12, 14] # list of integers in ascending order
x = 7 # number to insert
i = bisect.bisect(a, x) # call method
print(a)
print(i) # print on stdout the index where x value must be inserted
# output 3
bisect.insort(a, x)

print(a)