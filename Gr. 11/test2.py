mark1 = int (input ("Enter the mark for subject 1 :- "))
mark2 = int (input ("Enter the mark for subject 2 :- "))
mark3 = int (input ("Enter the mark for subject 3 :- "))
print ("Average marks is :- ", (mark1 + mark2 + mark3) / 3 )
per = ((mark1 + mark2 + mark3) / 300) * 100
print("Percentage :-",per)
if per >= 80 :
    print ("Grade is 'A'")
elif per >= 70 and per <= 79 :
    print ("Grade is 'B'")
elif per >= 60 and per <= 69 :
    print ("Grade is 'C'")
elif per >= 50 and per <= 59 :
    print ("Grade is 'D'")
elif per >= 40 and per <= 49 :
    print ("Grade is 'E'")
elif per <= 39 :
    print ("Grade is 'R'")