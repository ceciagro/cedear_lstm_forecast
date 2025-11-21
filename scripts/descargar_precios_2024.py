import yfinance as yf
import pandas as pd
import os

# Lista de tickers a descargar
tickers = [
    'NVDA', 'AAPL', 'PAM', 'GOOG', 'AMZN', 'TSLA', 'MSTR', 'SPY',
    'SPOT', 'QQQ', 'KO', 'DIA', 'META', 'BRK-B', 'PLTR', 'PEP',
    'GGAL', 'HUT', 'COIN', 'MRVL', 'PFE', 'AVGO', 'YPF'
]

# Rango de fechas a descargar
start_date = "2024-01-01"
end_date = "2024-12-31"

# Lista para acumular los DataFrames descargados
all_data = []

# Carpeta de salida
os.makedirs("data", exist_ok=True)
output_path = "data/processed/acciones_2024_limpio.csv"

# Descarga individual de cada ticker
for ticker in tickers:
    print(f"⬇️ Descargando: {ticker}")
    try:
        data = yf.download(ticker, start=start_date, end=end_date)

        if data.empty:
            print(f"⚠️ {ticker} no tiene datos.")
            continue

        # Agregar columna 'Price' basada en 'Close' redondeado
        data['Price'] = data['Close'].round(2)

        # Agregar columna con el nombre del ticker
        data['Ticker'] = ticker

        # Reiniciar el índice para obtener 'Date' como columna
        data = data.reset_index()

        # Seleccionar solo columnas útiles
        data = data[['Date', 'Ticker', 'Price']]

        all_data.append(data)

    except Exception as e:
        print(f"❌ Error con {ticker}: {e}")

# Concatenar todos los datos descargados
if all_data:
    final_df = pd.concat(all_data, ignore_index=True)

    # 🔍 En algunos entornos, las columnas pueden quedar como tuplas, las limpiamos:
    final_df.columns = [col[0] if isinstance(col, tuple) else col for col in final_df.columns]

    print(f"📋 Columnas en final_df: {list(final_df.columns)}")

    # Eliminar filas duplicadas por Date y Ticker
    final_df.drop_duplicates(subset=['Date', 'Ticker'], inplace=True)

    # Guardar el resultado como CSV
    final_df.to_csv(output_path, index=False)
    print(f"✅ Archivo guardado en: {output_path}")
else:
    print("⚠️ No se pudo guardar nada, todos los datasets estaban vacíos.")
