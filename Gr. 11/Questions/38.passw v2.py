while True:
    pw = input("Enter PASSWORD: ")
    if len(pw)<=8:
        print('The Password must have atleast 8 Characters.')
        continue
    up = no = spl = False
    s = '!@#$%^&*()_+|-=\\\'./'
    for i in pw:
        if i.isupper():
            up = True
            break
    for i in pw:
        if i.isdigit():
            no = True
            break
    for i in pw:
        if i in s:
            spl = True
            break
    if up == False:
        print('Your Password must have atleast one Upper case character.')
    if no == False:
        print('Your Password must have atleast one Number.')
    if spl == False:
        print('Your Password must have atleast one Special character.')