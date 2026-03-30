import pandas as pd

df = pd.read_csv('StudentsPerformance.csv')

# --- Tu código corregido ---

# Faltaba cerrar un paréntesis al final de .head(10))
print(df[['gender', 'race/ethnicity', 'parental level of education']].head(10))

# Aquí tenías un paréntesis de más o mal puesto al final
print(df['writing score'].tail(10))

# --- Nuevas instrucciones ---

# 1. Mostrar las columnas 'gender' y 'math score'
print(df[['gender', 'math score']])

# 2. Mostrar la cantidad de filas y columnas (shape)
print(f"Dimensiones (filas, columnas): {df.shape}")

# 3. Mostrar las primeras 4 filas
print(df.head(4))

# 4. Mostrar las últimas 4 filas
print(df.tail(4))
