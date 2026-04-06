import pandas as pd

# 1. Cargamos el archivo (con el nombre que tenés en VS Code)
df = pd.read_csv("StudentsPerformance.csv")

# 2. MOSTRAR INFO GENERAL (info)
print("--- Información general (info) ---")
df.info()

# 3. MOSTRAR LOS TIPOS DE DATOS DE TODO EL DATAFRAME (dtypes)
print("\n--- Tipos de datos (dtypes) ---")
print(df.dtypes)

# 4. MOSTRAR LAS COLUMNAS GENDER Y MATH SCORE
# (Ojo: fijate que en tu archivo están en minúsculas)
print("\n--- Columnas Gender y Math Score ---")
print(df[['gender', 'math score']])

# 5. MOSTRAR EL TIPO DE DATO DE LA COLUMNA GENDER
print("\n--- Tipo de dato de Gender ---")
print(df['gender'].dtype)

# 6. MOSTRAR SI HAY FILAS O COLUMNAS VACIAS (notnull)
print("\n--- Verificación de datos no vacíos (notnull) ---")
print(df.notnull())

# 7. MOSTRAR LA CANTIDAD DE FILAS Y COLUMNAS (shape)
print("\n--- Cantidad de filas y columnas (shape) ---")
print(df.shape)

# 8. MOSTRAR LAS ULTIMAS 5 FILAS (tail)
print("\n--- Últimas 5 filas ---")
print(df.tail())
