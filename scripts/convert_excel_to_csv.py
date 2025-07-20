# scripts/convert_excel_to_csv.py

import pandas as pd
import os

# Define rutas
input_file = "data/google-starttls-domains.xlsx"
output_file = "data/google-starttls-domains.csv"

# Verifica que el archivo exista
if not os.path.exists(input_file):
    raise FileNotFoundError(f"El archivo {input_file} no se encuentra.")

# Carga el archivo Excel
df = pd.read_excel(input_file)

# Guarda como CSV
df.to_csv(output_file, index=False)

print(f"Conversión completada: {output_file}")
