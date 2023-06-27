pw = input("Enter PASSWORD: ")
vd = False
no = (0,1,2,3,4,5,6,7,8,9)
up = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
spl = ('~','`','!','@','#','$','%','^','&','*','(',')','_','+','=',':',';')
if len(pw) < 7:
    vd = False
else:
    for i in pw:
        if i in no:
            vd = True
            break
        else:
            vd = False
    for i in pw:
        if i in up:
            vd = True
            break
        else:
            vd = False
    for i in pw:
        if i in spl:
            vd = True
            break
        else:
            vd = False
if vd == True:
    print('The Password is VALID.')
else:
    print('The Password is INVALID.')