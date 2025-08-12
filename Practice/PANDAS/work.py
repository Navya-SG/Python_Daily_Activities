#.groupby() [2] + .map() or .apply()
import pandas as pd
df=pd.read_json("data.json")
data = df.groupby(["role","gender"])["mark"].mean() #group by role and find mean of mark of grouped role
print(data)
df["data"]=df["role"].map(df.groupby("role")["mark"].mean()) #based on role assign the mean 
#df["data"] = df.apply(lambda row: data.get((row["role"], row["gender"])), axis=1)
print(df)
'''
#FA2025_NAVYA
JSON,CSV,ZIP HANDLING
multiple json files to single

create list
get user input

search/sort
binary
linear
bubble sort
seletion sort
qucik sort
insertion sort'''