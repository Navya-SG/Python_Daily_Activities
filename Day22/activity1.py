#Task1
import pandas as pd

cs = pd.read_csv('old_airline_data_2023.csv') #read csv file
js = pd.read_json('new_airline_data_2024.json') #read json file

null = js.isnull().sum() #check null places and count
print(null)

js.iloc[:,1:]=js.iloc[:,1:].fillna(js.iloc[:,1:].mean()) #replace empty place with mean
js=js.dropna() #drop empty column

#js['Month']=js['Month'].isin(['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']) #check and assign True if true

js.columns=js.columns.str.lower().str.replace(" ","_") 
js['month']=js['month'].str.capitalize() #error bcoz  8 line assign True to all rows of 1st col #month and not Month

new = js.groupby('month',as_index=False).first() #index not considered,only first occurance
print(new)

#Task2


