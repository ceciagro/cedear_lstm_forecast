# scripts/procesar_ccl.py

import pandas as pd
import os

# Ruta al archivo original
archivo_ccl = "data/raw/DOLARCCL.csv"

# Leer el CSV
df_ccl = pd.read_csv(archivo_ccl)

# Mostrar columnas detectadas para verificar
print("🧾 Columnas detectadas:", df_ccl.columns.tolist())

# Seleccionar y renombrar columnas necesarias
df_ccl = df_ccl[["fecha", "cierre"]].copy()
df_ccl.rename(columns={"fecha": "Date", "cierre": "CCL"}, inplace=True)

# Convertir la columna de fecha al tipo datetime
df_ccl["Date"] = pd.to_datetime(df_ccl["Date"], dayfirst=True, errors="coerce")

# Eliminar filas con valores nulos
df_ccl.dropna(subset=["Date", "CCL"], inplace=True)

# Ordenar por fecha
df_ccl.sort_values("Date", inplace=True)

# Reiniciar el índice
df_ccl.reset_index(drop=True, inplace=True)

# Vista previa del resultado
print("✅ CCL limpio:")
print(df_ccl.tail())

# Crear carpeta de salida si no existe
os.makedirs("data/processed", exist_ok=True)

# Guardar archivo limpio
df_ccl.to_csv("data/processed/CCL_limpio.csv", index=False)
print("💾 Archivo guardado en: data/processed/CCL_limpio.csv")
