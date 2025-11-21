import pandas as pd
import streamlit as st

# Cargar datos
df = pd.read_csv("data/processed/cedears_vs_inflacion_diario_2024.csv", parse_dates=["Date"])
df = df.sort_values(["Ticker", "Date"]).reset_index(drop=True)

tickers = df["Ticker"].unique().tolist()
fechas = df["Date"].dt.date.unique()

st.title("💼 Simulador de Inversión en CEDEARs 2024 por Período")

# Selección múltiple de tickers
tickers_seleccionados = st.multiselect("Seleccioná los CEDEARs que querés simular", tickers)

# Crear estructura para capturar parámetros por cada ticker
configuraciones = []

for ticker in tickers_seleccionados:
    st.markdown(f"### 🎯 Configuración para {ticker}")

    col1, col2, col3 = st.columns(3)

    with col1:
        fecha_ini = st.date_input(f"📅 Fecha inicio ({ticker})", min_value=min(fechas), max_value=max(fechas), key=f"{ticker}_ini")

    with col2:
        fecha_fin = st.date_input(f"📅 Fecha fin ({ticker})", min_value=min(fechas), max_value=max(fechas), key=f"{ticker}_fin")

    with col3:
        monto = st.number_input(f"💰 Monto a invertir ({ticker})", min_value=100.0, step=100.0, value=200000.0, key=f"{ticker}_monto")

    configuraciones.append({
        "Ticker": ticker,
        "Fecha Inicio": fecha_ini,
        "Fecha Fin": fecha_fin,
        "Monto": monto
    })

# Botón para calcular
if st.button("📊 Simular Inversión"):

    resultados = []

    for config in configuraciones:
        ticker = config["Ticker"]
        fecha_inicio = pd.to_datetime(config["Fecha Inicio"])
        fecha_fin = pd.to_datetime(config["Fecha Fin"])
        monto = config["Monto"]

        df_ticker = df[df["Ticker"] == ticker]

        fila_inicio = df_ticker[df_ticker["Date"] == fecha_inicio]
        fila_fin = df_ticker[df_ticker["Date"] == fecha_fin]

        if fila_inicio.empty or fila_fin.empty:
            st.warning(f"❌ Faltan datos para {ticker} en las fechas seleccionadas.")
            continue

        precio_ini = fila_inicio["Precio_CEDEAR_ARS"].values[0]
        precio_fin = fila_fin["Precio_CEDEAR_ARS"].values[0]

        cantidad = monto / precio_ini
        valor_final = cantidad * precio_fin
        ganancia = valor_final - monto
        rendimiento = (valor_final / monto - 1) * 100

        resultados.append({
            "Ticker": ticker,
            "Inicio": fecha_inicio.date(),
            "Fin": fecha_fin.date(),
            "Monto Invertido": round(monto, 2),
            "Precio Inicial": round(precio_ini, 2),
            "Precio Final": round(precio_fin, 2),
            "Valor Final": round(valor_final, 2),
            "Ganancia/Pérdida": round(ganancia, 2),
            "Rendimiento %": round(rendimiento, 2)
        })

    df_resultados = pd.DataFrame(resultados)
    st.subheader("📈 Resultados por CEDEAR")
    st.dataframe(df_resultados)

    if not df_resultados.empty:
        total_inv = df_resultados["Monto Invertido"].sum()
        total_valor = df_resultados["Valor Final"].sum()
        total_ganancia = total_valor - total_inv
        total_rend = (total_valor / total_inv - 1) * 100

        st.subheader("📌 Resumen General")
        st.markdown(f"""
        - 💰 **Total invertido:** ${total_inv:,.2f}  
        - 📈 **Valor final estimado:** ${total_valor:,.2f}  
        - 🧮 **Ganancia total:** ${total_ganancia:,.2f}  
        - 📊 **Rendimiento acumulado total:** {total_rend:.2f} %  
        """)

