# generar_dataset_diario.py

import pandas as pd

# Cargar precios diarios
df_precios = pd.read_csv("data/processed/precios_cedears_ars.csv")
df_precios["Date"] = pd.to_datetime(df_precios["Date"])

# Cargar inflación mensual
df_inflacion = pd.read_csv("data/processed/cedears_vs_inflacion_mensual_2024.csv")
df_inflacion["Mes"] = pd.to_datetime(df_inflacion["Mes"])

# Agregar columna 'Mes' a los precios para unir con inflación
df_precios["Mes"] = df_precios["Date"].dt.to_period("M").dt.to_timestamp()

# Unir por Ticker y Mes
df_diario = pd.merge(
    df_precios,
    df_inflacion[["Ticker", "Mes", "Inflacion_Mensual"]],
    on=["Ticker", "Mes"],
    how="left"
)

# Exportar a CSV
output_path = "data/processed/cedears_vs_inflacion_diario_2024.csv"
df_diario.to_csv(output_path, index=False)

print(f"✅ Archivo generado: {output_path}")
