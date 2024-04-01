with open('story.txt') as file:
    
    for i in file.readlines():print(i,type(i))
        







'''with open('yo.dat','wb+') as file:


    file.write(b'A woman finds a pot of treasure on the road.')
    file.seek(0)
    cont = file.read()



    print(cont)

    print(file.tell())

    print(file.seek(10))
    print(file.tell())
    file.seek(10,1)
    print(file.tell())
'''