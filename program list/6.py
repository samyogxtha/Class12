'''Write a program to read the contents of a text file line by line and write all the lines into another file except those line starting with ‘a’ or ‘A’.'''

try:
    with open('text.txt') as f:
        lines = f.readlines()
        new_lines=[]
        for i in lines:
            if i[0] not in 'aA':new_lines.append(i)
        with open('text1.txt','w') as f1:f1.writelines(new_lines)
except:print('File Not Found')