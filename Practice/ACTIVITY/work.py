#Task1
import pandas as pd
dc=pd.read_csv("old_airline_data_2023 (1).csv")
dj=pd.read_json("new_airline_data_2024 (1).json")
#print(dj)
print(dj.isnull().sum())
dj.iloc[:,1:]=dj.iloc[:,1:].fillna(dj.iloc[:,1:].mean())
#print(dj)
dj=dj.dropna()
#print(dj)
#dj["Month"]=dj["Month"].isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'])
#print(dj)
dj=dj.groupby("Month").first()
#dj = dj.drop_duplicates(subset='Month', keep='first')
print(dj)

map
reduce
filter
os module

2 or 3 zipfiles
each zipfile has 1000s of files  - use function
find extension
cluster and make one
same code again again not expected
use func
