import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import math
import os

# 🎨 Estilo visual
sns.set(style="whitegrid", palette="tab10")
os.makedirs("outputs", exist_ok=True)

# 📊 Cargar el archivo
df = pd.read_csv("data/processed/cedears_vs_inflacion_mensual_2024.csv", parse_dates=["Mes"])

# ✅ Asegurar columnas de porcentaje
df["Rendimiento_Mensual_%"] = df["Rendimiento"]
df["Inflacion_Mensual_%"] = df["Inflacion_Mensual"]

# 🔢 Dividir en grupos de 5 tickers
tickers = df["Ticker"].unique()
chunk_size = 5
chunks = [tickers[i:i + chunk_size] for i in range(0, len(tickers), chunk_size)]

# 🧮 Determinar cantidad de filas y columnas para los subplots
n_subplots = len(chunks)
cols = 2
rows = math.ceil(n_subplots / cols)

# 📐 Crear figura general con subplots
fig, axs = plt.subplots(rows, cols, figsize=(16, 6 * rows), sharex=True)

if n_subplots == 1:
    axs = [[axs]]
elif rows == 1:
    axs = [axs]

# 📈 Graficar cada grupo en su subplot
for idx, grupo in enumerate(chunks):
    row = idx // cols
    col = idx % cols
    ax = axs[row][col] if rows > 1 else axs[col]
    
    subset = df[df["Ticker"].isin(grupo)]
    sns.lineplot(data=subset, x="Mes", y="Rendimiento_Mensual_%", hue="Ticker", ax=ax, linewidth=1.5)
    
    inflacion = df.groupby("Mes")["Inflacion_Mensual_%"].mean().reset_index()
    ax.plot(inflacion["Mes"], inflacion["Inflacion_Mensual_%"], color="black", linestyle="--", label="Inflación Promedio")

    ax.set_title(f"Grupo {idx + 1}")
    ax.set_ylabel("Rendimiento Mensual (%)")
    ax.set_xlabel("Mes")
    ax.tick_params(axis='x', rotation=45)
    ax.grid(True)
    ax.legend(loc="upper left")

# 🔁 Si hay cuadrantes vacíos, los apagamos
for j in range(n_subplots, rows * cols):
    row = j // cols
    col = j % cols
    axs[row][col].axis('off')

# 💾 Ajustar y guardar
plt.suptitle("📈 Comparación Mensual: CEDEARs vs Inflación 2024", fontsize=16, y=0.92)
plt.tight_layout()
plt.subplots_adjust(top=0.92)
plt.savefig("outputs/cuadrantes_rendimiento_mensual.png", dpi=300)
plt.show()
print("✅ Todos los grupos graficados en cuadrantes y guardados como imagen.")
