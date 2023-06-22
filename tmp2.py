import datetime as dt

dob = '2006-10-07'
current_date = dt.date.today()
birth_date = dt.datetime.strptime(dob, '%Y-%m-%d').date()
age = current_date.year - birth_date.year - (current_date.month < birth_date.month or (current_date.month == birth_date.month and current_date.day < birth_date.day))

print(age)