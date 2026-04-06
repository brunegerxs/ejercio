import pandas as pd

# 1. ABRIR EL CSV
df = pd.read_csv("StudentsPerformance.csv")

# 2. MOSTRAR LAS 3 ULTIMAS COLUMNAS (poniendo los nombres)
print("--- Últimas 3 columnas ---")
print(df[['reading score', 'writing score', 'math score']])

# 3. MOSTRAR LAS 100 PRIMERAS FILAS
print("\n--- Primeras 100 filas ---")
print(df.head(100))

# 4. MOSTRAR LA CANTIDAD DE COLUMNAS (con shape)
print("\n--- Cantidad de filas y columnas ---")
print(df.shape)

# 5. MOSTRAR SI HAY FILAS VACIAS (usando notnull como antes)
print("\n--- Verificación de datos (notnull) ---")
print(df.notnull())

# 6. MOSTRAR LOS DIFERENTES TIPOS DE DATOS (dtypes)
print("\n--- Tipos de datos de las columnas ---")
print(df.dtypes)
