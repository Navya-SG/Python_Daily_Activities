from datetime import date, datetime

doj=input("Enter date of joining(YYYY-MM-DD):")
date_join=datetime.strptime(doj,"%Y-%m-%d").date()
date_curr=date.today()

days_comp=(date_curr - date_join).days
years_comp=days_comp//365
mon_comp=years_comp//12
print("Days completed:",days_comp)
print(f"Approximate number of {years_comp} years and {mon_comp} months")



