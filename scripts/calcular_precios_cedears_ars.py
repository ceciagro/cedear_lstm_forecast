# scripts/calcular_precios_cedears_ars.py

import pandas as pd
import os

print("📥 Cargando archivos...")

# Rutas de entrada
acciones_path = "data/processed/acciones_2024_limpio.csv"
ccl_path = "data/processed/CCL_limpio.csv"
ratios_path = "data/processed/ratios_cedears.csv"

# Leer datasets
acciones_df = pd.read_csv(acciones_path, parse_dates=["Date"])
ccl_df = pd.read_csv(ccl_path, parse_dates=["Date"])
ratios_df = pd.read_csv(ratios_path)

# Normalizar nombres de columnas
ratios_df.rename(columns={"ticker": "Ticker", "cedears_ratio": "Ratio"}, inplace=True)

# Asegurar que los tickers estén en mayúscula
acciones_df["Ticker"] = acciones_df["Ticker"].str.upper()
ratios_df["Ticker"] = ratios_df["Ticker"].str.upper()

# 🔄 Unir ratios a acciones
acciones_df = acciones_df.merge(ratios_df, on="Ticker", how="left")

# 🔄 Unir CCL por fecha
acciones_df = acciones_df.merge(ccl_df, on="Date", how="left")

# 🧼 Rellenar CCL faltantes con el último valor válido
nulos_antes = acciones_df["CCL"].isna().sum()
acciones_df["CCL"] = acciones_df["CCL"].fillna(method="ffill")
nulos_despues = acciones_df["CCL"].isna().sum()
print(f"🧮 Nulos en CCL antes: {nulos_antes} | después: {nulos_despues}")

# Calcular el precio estimado en ARS de cada CEDEAR
acciones_df["Precio_CEDEAR_ARS"] = (acciones_df["Price"] * acciones_df["CCL"]) / acciones_df["Ratio"]

# Validar resultados
print("✅ Muestra del resultado final:")
print(acciones_df[["Date", "Ticker", "Price", "Ratio", "CCL", "Precio_CEDEAR_ARS"]].tail())

# Guardar resultado
os.makedirs("data/processed", exist_ok=True)
acciones_df.to_csv("data/processed/precios_cedears_ars.csv", index=False)
print("💾 Archivo guardado en: data/processed/precios_cedears_ars.csv")

# 🔎 Diagnóstico de valores faltantes por Ticker
resumen_nulos = acciones_df.groupby("Ticker").agg(
    total_registros=("CCL", "count"),
    registros_nan=("CCL", lambda x: x.isna().sum())
)
resumen_nulos["porcentaje_nan"] = resumen_nulos["registros_nan"] / (resumen_nulos["total_registros"] + resumen_nulos["registros_nan"]) * 100
resumen_nulos = resumen_nulos.sort_values("porcentaje_nan", ascending=False)

# Mostrar resumen en consola
print("\n📊 Diagnóstico de datos faltantes por Ticker:")
print(resumen_nulos)

# Guardar el resumen como CSV
resumen_nulos.to_csv("data/processed/resumen_nulos_ccl.csv")
print("💾 Archivo resumen guardado en: data/processed/resumen_nulos_ccl.csv")
