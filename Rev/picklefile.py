import pickle,tabulate

with open('picklefile.dat','ab') as file:
    pickle.dump(['100', 'Ram', 'Admin', 'Admin', '20000'],file)
    pickle.dump(['200', 'Samy', 'Teacher ', 'Commerce', '16000'],file)

with open('picklefile.dat','rb') as file:
    content = []
    while True:
        try:content.append(pickle.load(file))
        except:break

    print(tabulate.tabulate(content,headers=['no','no','no','no','no']))
    for i in content:print(i)