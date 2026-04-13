import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

print(df[['gender', 'math score']])
print(df[['gender, math score']].shape)
print(df.head(8))
print(df.tail(4))