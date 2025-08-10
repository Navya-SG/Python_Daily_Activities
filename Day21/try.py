import pandas as pd
import numpy as np
df = pd.read_csv('students.csv')
filtered = df[(df['gender']=='male')(df['class'].isin(['Four','Five'])) &(df['mark']>70)]
print(filtered)
