# scripts/generar_inflacion_csv.py

import pandas as pd
import os

# Crear el DataFrame con meses ya en inglés y en formato estándar
data = {
    "Mes": [
        "Jan 2024", "Feb 2024", "Mar 2024", "Apr 2024", "May 2024", "Jun 2024",
        "Jul 2024", "Aug 2024", "Sep 2024", "Oct 2024", "Nov 2024", "Dec 2024"
    ],
    "Inflacion_Mensual": [
        20.6, 13.2, 11.0, 8.8, 4.2, 4.6, 3.9, 3.6, 3.4, 3.3, 3.2, 3.1
    ]
}

df = pd.DataFrame(data)

# Crear carpeta si no existe
os.makedirs("data/processed", exist_ok=True)

# Guardar como CSV
df.to_csv("data/processed/inflacion_mensual_2024.csv", index=False)
print("✅ Archivo guardado en: data/processed/inflacion_mensual_2024.csv")
