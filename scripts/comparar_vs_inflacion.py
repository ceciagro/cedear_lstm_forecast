import pandas as pd
import os

print("📊 Cargando datos...")

# Cargar precios de CEDEARs
precios_df = pd.read_csv("data/processed/precios_cedears_ars.csv", parse_dates=["Date"])

# Cargar inflación mensual
inflacion_df = pd.read_csv("data/processed/inflacion_mensual_2024.csv")

# Normalizar nombres de mes y convertir a datetime
inflacion_df["Mes"] = inflacion_df["Mes"].str.strip().str.title()
inflacion_df["Mes"] = pd.to_datetime(inflacion_df["Mes"], format="%b %Y")

# Convertir inflación a formato decimal si hace falta
if inflacion_df["Inflacion_Mensual"].max() > 1:
    inflacion_df["Inflacion_Mensual"] = inflacion_df["Inflacion_Mensual"] / 100

# Crear columna de mes en precios_df
precios_df["Mes"] = precios_df["Date"].dt.to_period("M").dt.to_timestamp()

# Calcular precios inicial y final por Ticker y Mes
precios_mensuales = precios_df.groupby(["Ticker", "Mes"]).agg(
    Precio_Inicial=("Precio_CEDEAR_ARS", "first"),
    Precio_Final=("Precio_CEDEAR_ARS", "last")
).reset_index()

# Calcular rendimiento mensual
precios_mensuales["Rendimiento"] = precios_mensuales["Precio_Final"] / precios_mensuales["Precio_Inicial"] - 1

# Calcular rendimiento acumulado por ticker
rend_acumulado = precios_mensuales.groupby("Ticker")["Rendimiento"].apply(
    lambda r: (1 + r).prod() - 1
).reset_index().rename(columns={"Rendimiento": "Rendimiento_Acumulado_2024"})

# Calcular inflación acumulada
inflacion_acumulada = (1 + inflacion_df["Inflacion_Mensual"]).prod() - 1

# Unir inflación mensual
comparacion = precios_mensuales.merge(inflacion_df, on="Mes", how="left")

# Comparar rendimiento mensual vs inflación mensual
comparacion["Le_Gano_A_Inflacion"] = comparacion["Rendimiento"] > comparacion["Inflacion_Mensual"]

# Agregar rendimiento acumulado por ticker
comparacion = comparacion.merge(rend_acumulado, on="Ticker", how="left")

# Agregar inflación acumulada como columna fija
comparacion["Inflacion_Acumulada_2024"] = inflacion_acumulada

# Convertir a porcentaje con 2 decimales
comparacion["Rendimiento"] = (comparacion["Rendimiento"] * 100).round(2)
comparacion["Inflacion_Mensual"] = (comparacion["Inflacion_Mensual"] * 100).round(2)
comparacion["Rendimiento_Acumulado_2024"] = (comparacion["Rendimiento_Acumulado_2024"] * 100).round(2)
comparacion["Inflacion_Acumulada_2024"] = (comparacion["Inflacion_Acumulada_2024"] * 100).round(2)

# Vista previa
print("✅ Comparación mensual + acumulada:")
print(comparacion.head())

# Guardar resultado
os.makedirs("data/processed", exist_ok=True)
comparacion.to_csv("data/processed/cedears_vs_inflacion_mensual_2024.csv", index=False)
print("💾 Archivo guardado: data/processed/cedears_vs_inflacion_mensual_2024.csv")
