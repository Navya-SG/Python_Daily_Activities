#series-1D array like obj
import pandas as pd
data = pd.Series([1,2,3,4,5])
print(data)

#series from dict
import pandas as pd
data = {'a':100,'b':200,'c':300}
s = pd.Series(data)
print(s)

#series with customized index
import pandas as pd
s = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s)

#access elements using index
import pandas as pd
s = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s['b']) #2

#access elements using integer position
import pandas as pd
s = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s[3]) #4

#boolean condition
import pandas as pd
s = pd.Series([1,2,3,4],index=['a','b','c','d'])
print(s>2) # a False b False c True d True

#DataFrame int
import pandas as pd
data = {'yes':[50,21],'No':[131,2]}
s = pd.DataFrame(data)
print(s)
#    yes   No
 0   50  131
 1   21    2

#DataFrame str
import pandas as pd
data = {'Bob': ['I liked it.', 'It was awful.'], 'Sue': ['Pretty good.', 'Bland.']}
s = pd.DataFrame(data)
print(s)
#             Bob           Sue
 0    I liked it.  Pretty good.
 1  It was awful.        Bland.

#read CSV file
import pandas as pd
c_file = pd.read_csv("data.csv")
print(c_file)

#read CSV file using delimiter
import pandas as pd
c_file = pd.read_csv("data.csv",delimiter=';')
print(c_file)

#read JSON file (entire file is a single JSON object)
data=>[
  {"name": "Alice", "age": 25},
  {"name": "Bob", "age": 30}
]
import pandas as pd
j_file = pd.read_json("data.json")
print(j_file)

#read JSON file(each line is a seperate json object) - seperate dicts
data=>{"name": "Alice", "age": 25}
      {"name": "Bob", "age": 30}
import pandas as pd
J_file = pd.read_json("data.json", lines=True)
print(J_file)

#data type
import pandas as pd
df = pd.DataFrame({
    'name': ['Alice', 'Bob'],
    'age': [25, 30],
    'height': [5.5, 6.0],
    'is_student': [True, False],
    'enroll_date': pd.to_datetime(['2023-01-01', '2023-06-15']),
    'grade': pd.Series(['A', 'B'], dtype='category') #must include to tell that it is category type
})
print(df.dtypes)

# type casting
data=> [{"name": "Navya", "role": "Engineer", "mark":50.0},
	{"name": "gokila", "role": "teacher","mark":5.0}]
import pandas as pd
df=pd.read_json("data.json")
df["mark"]=df["mark"].astype(int)
print(df["mark"])

#type casting to category
import pandas as pd
df=pd.read_json("data.json")
df["mark"]=df["mark"].astype('category')
print(df["mark"])
O.T: 0    50
     1     5
     Name: mark, dtype: category
     Categories (2, int64): [5, 50]

#DF essentials
import pandas as pd
df=pd.read_json("data.json")
print(df.shape) #(2, 3)
print(df.columns) #Index(['name', 'role', 'mark'], dtype='object')
print(df.index) #RangeIndex(start=0, stop=2, step=1)

# .head()/.tail() - return no of rows
import pandas as pd
df=pd.read_json("data.json")
print(df.head()) #first 5 rows
print(df.tail()) #last 5 rows
#customized
print(df.head(3)) #first 3 rows
print(df.tail(7)) #last 7 rows

# .info() - all details
import pandas as pd
df=pd.read_json("data.json")
print(df.info())
OT: <class 'pandas.core.frame.DataFrame'>
RangeIndex: 12 entries, 0 to 11
Data columns (total 3 columns):
 #   Column  Non-Null Count  Dtype
---  ------  --------------  -----
 0   name    12 non-null     object
 1   role    12 non-null     object
 2   mark    12 non-null     float64
dtypes: float64(1), object(2)
memory usage: 420.0+ bytes
None

# .describe() NUMERIC - checks(count,mean,std,min,25%,50%,75%,max) of NUMERIC data
import pandas as pd
df=pd.read_json("data.json")
print(df.describe())
OT:            mark
count  12.000000
mean   64.500000
std    23.628758
min     5.000000
25%    53.750000
50%    70.750000
75%    79.000000
max    91.000000

# .describe()NON-NUMERIC - checks(count,uniq,top,freq) of NON-NUMERIC data
import pandas as pd
df=pd.read_json("data.json")
print(df.describe(include='object'))
OT:          name      role
count      12        12
unique     12         9
top     Navya  Engineer
freq        1         3

# .mean (mean)
import pandas as pd
df=pd.read_json("data.json")
print(df["mark"].mean()) #64.5

# .unique() (unique values)
import pandas as pd
df=pd.read_json("data.json")
print(df["name"].unique()) #['Navya' 'Gokila' 'Arjun' 'Meera' 'Ravi' 			    'Sneha' 'Kiran' 'Divya' 'Amit' 'Priya'  			    'Vikram' 'Neha']

# .value_counts()(count of all values)
import pandas as pd
df=pd.read_json("data.json")
print(df["role"].value_counts()) 
#role
Engineer          3
Teacher           2
Data Scientist    1
Designer          1
Manager           1
HR                1
Developer         1
Analyst           1
Consultant        1

#check index
import pandas as pd
df=pd.read_json("data.json")
print(df.index)

#ACCESS COLUMNS
#access single column []
import pandas as pd
df=pd.read_json("data.json")
print(df["role"])

#access multiple columns [[]]
import pandas as pd
df=pd.read_json("data.json")
print(df[["role","mark"]])

#ACCESS ROWS
#using labels (nth row, xxx column)
import pandas as pd
df=pd.read_json("data.json")
print(df.loc[0,"mark"]) #0th row, mark column 

#complete row
print(df.loc[0]) #0th row

#using integer labels (nth row, nth column)
import pandas as pd
df=pd.read_json("data.json")
print(df.iloc[0,2]) #0th row, 2nd column 

#complete row
import pandas as pd
df=pd.read_json("data.json")
print(df.iloc[0]) #0th row

#using slicing
print(df.iloc[1:4]) #row 1,2,3

#ACCESS using index 
#customize column value as index
inplace=True->data is reflected in main data 
              if not used -> creates duplicate data with the index
import pandas as pd
df=pd.read_json("data.json")
df.set_index("mark",inplace=True) #uses mark column as index
print(df.loc[50.0]) #access using value

#reset_index
import pandas as pd
df=pd.read_json("data.json")
df.reset_index(inplace=True) #resets to default index

#assign data
import pandas as pd
df=pd.read_json("data.json")
df["Passed"]=True #create new table passed and add True as values
print(df["Passed"])

import pandas as pd
df=pd.read_json("data.json")
df["bonus"]=[500,400,300,500,200,100,233,232,400,200,500,300] #create new table bonus and add the values given
print(df)

import pandas as pd
df=pd.read_json("data.json")
df["paid"]=[50 if mark>50 else 20 for mark in df['mark']] #create new table paid and add values as per condition
print(df)

#filter rows
import pandas as pd
df=pd.read_json("data.json")
score = df["mark"] > 60
print(score) #index with True or False
scores = df[df["mark"] > 60]
print(scores) # all the data that satisfies condition
role = df[df["role"] == "Engineer"]
print(role) # all the data that satisfies condition
roles_and = df[(df["role"] == "Engineer") & (df["mark"] > 55)]
print(roles_and) # all the data that satisfies condition
roles_or = df[(df["role"] == "Engineer") | (df["role"] == "Teacher")]
print(roles_or) # all the data that satisfies condition
roles_nor = df[~(df['role'] == 'Engineer')]
print(roles_nor) # all the data that satisfies condition

#.isin([" "," "]) filter
import pandas as pd
df=pd.read_json("data.json")
roles = df[df["role"].isin(["Engineer","Teacher"])]
print(roles) # all the data in -> isin()

#query-filter of rows
import pandas as pd
df=pd.read_json("data.json")
data = df.query('role=="Engineer" and mark>50')

==> id we have any col name "class", it is a python keywork so to avoid minstrupt use `class`

#map() - (element wise mapping) function that transforms values from one form to another(works on Series)
import pandas as pd
df=pd.read_json("data.json")
df['mark'] = df['mark'].map(lambda x: x + 5)
print(df) #add 5 to marks

#map() - error
import pandas as pd
df=pd.read_json("data.json")
df['role'] = df['role'].map({'Engineer': 'Er', 'Teacher': 'Tr'})
print(df) #other roles will get "NaN"

#Solution
import pandas as pd
df=pd.read_json("data.json")
df['role'] = df['role'].replace({'Engineer': 'Er', 'Teacher': 'Tr'})
print(df) #other roles will not be modified

#.apply() solution
import pandas as pd
df=pd.read_json("data.json")
df['role'] = df['role'].apply(lambda x: {'Engineer': 'Er', 'Teacher': 'Tr'}.get(x, x))
print(df)

#.apply() - (apply a function to each element (or row/column) in a DataFrame or Series)
import pandas as pd
df=pd.read_json("data.json")
def grade(row):
    if row['mark'] >= 90:
        return 'A'
    elif row['mark'] >= 75:
        return 'B'
    elif row['mark'] >= 60:
        return 'C'
    else:
        return 'D'
df['grade'] = df.apply(grade, axis=1)
print(df["grade"])

#.apply with numpy for column wise
import pandas as pd
import numpy as np
df=pd.read_json("data.json")
df[["mark"]].apply([np.mean,np.std]) #[[]]
print(df["mark"])

#.groupby()
#.groupby() + .map()
import pandas as pd
df=pd.read_json("data.json")
data = df.groupby("role")["mark"].mean() #group by role and find mean of mark of grouped role
print(data)
df["data"]=df["role"].map(data) #based on role assign the mean 
print(df)

#.groupby() [2] + .map() or .apply()
import pandas as pd
df=pd.read_json("data.json")
data = df.groupby(["role","gender"])["mark"].mean() #group by role and find mean of mark of grouped role
print(data)
df["data"]=df["role"].map(df.groupby("role")["mark"].mean()) #based on role assign the mean 
#df["data"] = df.apply(lambda row: data.get((row["role"], row["gender"])), axis=1)
print(df)

#.agg()
import pandas as pd
df=pd.read_json("data.json")
data = df.groupby('role')['mark'].agg(['mean','max'])
df["data"]=df["role"].map(data)
print(df)

#SORTING
#by single col - ascending
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_values("mark") or df.sort_values(by="mark")
print(sort)

#by single col - descending
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_values("mark", ascending=False or df.sort_values(by="mark",ascending=False)
print(sort)

#by multiple cols - 1st-asc,2nd-desc
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_values(['role','mark'],ascending=[True,False]) or df.sort_values(by=["role","mark"],ascending=[True,False])
print(sort)

#by multiple cols - 1st-desc,2nd-asc
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_values(['role','mark'],ascending=[False,True]) or df.sort_values(by=["role","mark"],ascending=[False,True])
print(sort)

#sort by index
#ascending
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_index()
print(sort)

#descending
#by index
import pandas as pd
df=pd.read_json("data.json")
sort = df.sort_index(ascending=False)
print(sort)

#MISSING VALUES HANDLING
#find null(True/False)
import pandas as pd
df=pd.read_json("data.json")
null = df.isnull()
print(null)#if null= True, else False

#count null
import pandas as pd
df=pd.read_json("data.json")
null = df.isnull().sum()
print(null)#adds all null value
OT:
name      1
role      1
mark      1
gender    0
dtype: int64

#remove missing data row
import pandas as pd
df=pd.read_json("data.json")
null = df.dropna()
print(null)#only True values are printed

#remove missing data column
import pandas as pd
df=pd.read_json("data.json")
null = df.dropna(axis=1)
print(null)#the columns will no null values only printed

#fill missing data with 0
import pandas as pd
df=pd.read_json("data.json")
df["mark"]=df["mark"].fillna(0)
print(df)#the null space is filled with 0 other null spaces are NaN

#fill missing data with string
import pandas as pd
df=pd.read_json("data.json")
df["name"]=df["name"].fillna('unknown')
print(df)#the null space is filled with 'unknown' other null spaces are NaN

#fill missing data with mean/median/mode
import pandas as pd
df=pd.read_json("data.json")
df["mark"]=df["mark"].fillna(df["mark"].mean())
print(df)#the null space is filled with mean of mark column other null spaces are NaN

#fill missing data with last non-null value
import pandas as pd
df=pd.read_json("data.json")
df.fillna(method='ffill',inplace=True) #inplace=True: Tells pandas to modify the original DataFrame directly, without returning a new one.
print(df)#the null space is filled with last non-null value

#fill missing data with next non-null value
import pandas as pd
df=pd.read_json("data.json")
df.fillna(method='bfill',inplace=True) #inplace=True: Tells pandas to modify the original DataFrame directly, without returning a new one.
print(df)#the null space is filled with last non-null value'

# .rename(columns={" ":" "}) -> rename column
import pandas as pd
df=pd.read_json("data.json")
df_renamed=df.rename(columns={"mark":"score"})
print(df_renamed)

# .rename(index={index_num:" "}) -> rename index
import pandas as pd
df=pd.read_json("data.json")
df_index_renamed=df.rename(index={0:'name1'})
print(df_index_renamed) #index 0 changed to name1

#concat with(ignore_index=True)
import pandas as pd
s=pd.DataFrame({"id":[1,2,3],
		"mark":[10,20,30]})
d=pd.DataFrame({"id":[1,2,3],
		"name":["n","a","v"]})
conc = pd.concat([s,d],ignore_index=True)
print(conc)
OT:
   id  mark name
0   1  10.0  NaN
1   2  20.0  NaN
2   3  30.0  NaN
3   1   NaN    n
4   2   NaN    a
5   3   NaN    v

#concat without(ignore_index=True)
import pandas as pd
s=pd.DataFrame({"id":[1,2,3],
		"mark":[10,20,30]})
d=pd.DataFrame({"id":[1,2,3],
		"name":["n","a","v"]})
conc = pd.concat([s,d],ignore_index=True)
print(conc)
OT:
   id  mark name
0   1  10.0  NaN
1   2  20.0  NaN
2   3  30.0  NaN
0   1   NaN    n
1   2   NaN    a
2   3   NaN    v

#concat DataFrames (axis=1 for cols and rows matched)
import pandas as pd
df1 = pd.DataFrame({
    'name': ['Tom', 'Jerry'],
    'mark': [80, 95]})
df2 = pd.DataFrame({
    'gender': ['M', 'M'],
    'grade': ['A', 'A+']})
df_merged = pd.concat([df1, df2], axis=1)
print(df_merged)
OT:
    name  mark gender grade
0    Tom    80      M     A
1  Jerry    95      M    A+
OT:(without axis=1)
    name  mark gender grade
0    Tom  80.0    NaN   NaN
1  Jerry  95.0    NaN   NaN
0    NaN   NaN      M     A
1    NaN   NaN      M    A+

#merge DataFrames (pd.merge(DF1,DF2,"matching_col_name"))
import pandas as pd
s=pd.DataFrame({"id":[1,2,3],
		"mark":[10,20,30]})
d=pd.DataFrame({"id":[1,2,3],
		"name":["n","a","v"]})
mer = pd.merge(s,d,on="id")
print(mer)

#join DataFrames (DF1.join(DF2))
import pandas as pd
df=pd.read_json("data.json")
df1 = df.set_index('name')
df2 = pd.DataFrame({
    'grade': ['A', 'B'],
}, index=['Navya', 'Gokila'])
joined = df1.join(df2)
print(joined) #set col as index and select row to that col as index to join values

#to reset column as index
import pandas as pd
df=pd.read_json("data.json")
df1 = df.set_index('name')
reset=df1.reset_index()
print(df)

#drop duplicates
import pandas as pd
import json
df1 = pd.read_json("file1.json")
df2 = pd.read_json("file2.json")
df3 = pd.read_json("file3.json")
combined_df = pd.concat([df1, df2, df3], ignore_index=True)
clean_df = combined_df.drop_duplicates()
print(clean_df)

# drop duplicates of columns
df.drop_duplicates(subset=['name'])
