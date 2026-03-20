import pandas as pd
df=pd.read_csv('StudentsPerformance.csv')
print(df['gender'])
print(df['gender'].head())
print(df['lunch'].head(12))
print(df['gender'].tail(12))
print(df['lunch'].tail(12))
