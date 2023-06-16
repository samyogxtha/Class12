def REVERSAR(Number):
    reversed_number = 0
    
    while Number > 0:
        remainder = Number % 10
        reversed_number = (reversed_number * 10) + remainder
        Number = Number // 10
    return reversed_number

def reversar2(number):
    num = list(str(number))
    num.reverse()
    rstr = ''
    for i in num:
        rstr += i
    return rstr

print(REVERSAR(1543))
