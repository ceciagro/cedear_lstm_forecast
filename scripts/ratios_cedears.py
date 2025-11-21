import os
import pandas as pd

# Crear carpeta si no existe
os.makedirs("data", exist_ok=True)

# Diccionario de ratios CEDEAR
ratios = {
    "NVDA": 10,
    "AAPL": 10,
    "PAM": 25,
    "GOOG": 29,
    "AMZN": 144,
    "TSLA": 15,
    "MSTR": 20,
    "SPY": 10,
    "SPOT": 5,
    "QQQ": 10,
    "KO": 5,
    "DIA": 3,
    "META": 30,
    "BRK-B": 20,
    "PLTR": 3,
    "PEP": 3,
    "GGAL": 10,
    "HUT": 30,
    "COIN": 10,
    "MRVL": 3,
    "PFE": 5,
    "AVGO": 20,
    "YPF": 3
}

# Convertir a DataFrame
df_ratios = pd.DataFrame(list(ratios.items()), columns=["Ticker", "cedears_ratio"])

# Guardar como CSV
ruta_salida = "data/processed/ratios_cedears.csv"
df_ratios.to_csv(ruta_salida, index=False)

print(f"✅ Archivo creado en {ruta_salida}")
