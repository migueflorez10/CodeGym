# ==========================================
# 1. Importar librerías
# ==========================================
import pandas as pd
import os

# ==========================================
# 2. Definir ruta del dataset
# ==========================================
path = "/Users/migueflorez10/.cache/kagglehub/datasets/mohammadtalib786/retail-sales-dataset/versions/1"

# ==========================================
# 3. Verificar archivos disponibles
# ==========================================
print("Archivos en el dataset:")
print(os.listdir(path))

# ==========================================
# 4. Cargar dataset
# ==========================================
df = pd.read_csv(path + "/retail_sales_dataset.csv")

df.head()
df.info()
df.isnull().sum()
df = df.drop_duplicates()
df = df.dropna(subset=['Customer ID', 'Total Amount'])
df = df[df['Total Amount'] > 0]
df['Product Category'] = df['Product Category'].str.upper()
df[df.duplicated(subset=['Transaction ID'], keep=False)]
df_clean = df.copy()
print(df_clean['Total Amount'].sum())
