import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv('StudentsPerformance.csv')


print(df[['reading score', 'math score']])
x = df['reading score']
y = df['math score']
plt.plot(x,y)
plt.show()