def bla():
    with open('text.txt','w+')as file:
        words='a pot of treasure'
        lis=['a\n','clever\n','monkey\n']

        file.write(words)
        file.writelines(lis)

        file.seek(0)

        newwords = file.read()
        file.seek(0)
        newlist = file.readlines()

        

        print(newwords)
        print(newlist)

bla