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

11-2
11.30 - 2.30


class Car:
    brand = "Toyota"  
    def __init__(self,number_plate):
        self.number_plate = number_plate  
car1=Car("XXXXX")
car2=Car("YYYYY")
print(car1.brand,car1.number_plate) 
print(car2.brand,car2.number_plate)