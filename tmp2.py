from datetime import date
def calculateAge(birthDate):
       today = date.today()
       age = today.year - birthDate.year - ((today.month, today.day) <  (birthDate.month, birthDate.day))
       return age
print(calculateAge(date(2006, 10, 7)), "years")