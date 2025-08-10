import pandas as pd
df = pd.read_csv('student.csv')
filtered = df[(df['gender']=='male')&
              (df['class'].isin(['Four','Five']))&
              (df['mark']>70)]
print(filtered)