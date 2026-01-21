import pandas as pd 
import os 

path = "/Users/migueflorez10/.cache/kagglehub/datasets/mehmettahiraslan/customer-shopping-dataset/versions/2"

print('Archivos en el dataset: ')
print(os.listdir(path)) # Observamos que archivos hay en la ruta path

df = pd.read_csv(path + '/customer_shopping_data.csv') # leo el csv con pandas y lo transformo en un dataframe para poder manipularlo

print(df.head()) # me proporcina la informacion de las primeras 5 filas del dataframe
print(df.info()) # me muestra un resumen tecnico del dataframe, # filas, # de columnas, nombres de las columnas, tipos de datos, etc.
print(df.isnull().sum()) # busca en cada fila si hay valores nulos, si los hay pone true, de lo contrario false y los suma.

print(df.drop_duplicates(subset=['invoice_no']))
print('Los valores duplicados de customer_id son: ',df['customer_id'].isnull().sum())
print(((df['age'] >= 18 ) & (df['age'] <= 100) ))
print((df['quantity']>0).all())
print((df['price'] > 0).all())
df['category'] = df['category'].str.upper()
print(df['category'].head())
