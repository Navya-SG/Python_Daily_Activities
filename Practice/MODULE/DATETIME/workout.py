#current
import datetime as dt
now = dt.datetime.now()
print(now)
print(now.year,now.month,now.day,now.hour,now.minute,now.second)

#time manual
from datetime import time
t=time(10,12,30)
print(t)
print(t.hour,t.minute,t.second)

#manual date,time
import datetime as dt
now = dt.datetime(2025,8,9,17,30)
print(now)

#today
from datetime import date
today = date.today()
print(today)

#date manual
from datetime import date
d = date(2025,8,9)
print(d.year,d.month,d.day)

#activity
from datetime import date, datetime
doj=input("Enter date of joining(YYYY-MM-DD):")
date_join=datetime.strptime(doj,"%Y-%m-%d").date()
date_curr=date.today()
days_comp=(date_curr - date_join).days
years_comp=days_comp//365
mon_comp=years_comp//12
print("Days completed:",days_comp)
print(f"Approximate number of {years_comp} years and {mon_comp} months")