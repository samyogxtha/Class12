import csv

#with open('yo.csv',newline='') as file:
#    myreader=(csv.reader(file,delimiter=','))
#    for i in myreader:
#        print (i)
#
#with open('yo.csv','a',newline='') as file:
#    mywriter = csv.writer(file,delimiter=',')
#    if file.tell()==0:mywriter.writerow(['id','name','job','sal'])
#
#    mywriter.writerows([['100', 'Ram', 'Admin', 'Admin', '20000'], ['200', 'Samy', 'Teacher ', 'Commerce', '16000']])
#    mywriter.writerow([300,'Yoo','Teacher','Com',1600])
#    mywriter.writerows([[400,'Yoo','Teacher','Com',21000],[500,'Yoo','Teacher','Com',1700]])

d={'empno':1,'sal':2000}
with open('emp.csv','w+',newline='') as file:
    writer=csv.DictWriter(file,fieldnames=d.keys())  
    writer.writeheader()
    writer.writerow(d)

    file.seek(0)
    reader=list(csv.DictReader(file))

    for i in reader:
        print(i)
