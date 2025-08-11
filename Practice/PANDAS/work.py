#join DataFrames (DF1.join(DF2))
import pandas as pd
df=pd.read_json("data.json")
df1 = df.set_index('name')
df2 = pd.DataFrame({
    'grade': ['A', 'B'],
}, index=['Navya', 'Gokila'])
joined = df1.join(df2)
print(joined) #set col as index and select row to that col as index to join values

#FA2025_NAVYA