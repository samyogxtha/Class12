from datetime import datetime as dt

res = (dt.strptime('2023-07-23', "%Y-%m-%d") - dt.strptime('2023-07-27', "%Y-%m-%d")).days
print(res)