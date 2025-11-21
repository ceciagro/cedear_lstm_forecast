
<p align="center">
  <img src="assets/banner_cedear_forecast.png" alt="CEDEARs Forecasting Banner" width="100%">
</p>

# 💰 Precios y Rendimientos de CEDEARs: Deep Learning (LSTM) para Estrategia Financiera

**Author:** Cecilia Ledesma  
**GitHub:** https://github.com/ceciagro  
**Role:** Data Scientist – Portfolio Project: Advanced Time Series

## 🔗 Dataset Source & Context

Este proyecto utiliza precios históricos de acciones y datos del mercado financiero argentino para generar la base de predicción.

- **Fuente de Precios:** Yahoo Finance (vía `yfinance`).
- **Datos Secundarios:** Cotizaciones del tipo de cambio Contado con Liquidación (CCL) y datos de inflación histórica.
- **Contexto:** Enfoque en la volatilidad de los CEDEARs en pesos argentinos y su rendimiento ajustado por inflación.

---

## 🚀 1. Project Overview: De la Historia al Pronóstico

Este proyecto evoluciona de un análisis histórico (Fase 1) a una **solución de pronóstico robusta** (Fase 2) que utiliza Deep Learning para la toma de decisiones de inversión.

El objetivo central es:

### **“¿Cómo se puede pronosticar el rendimiento real de un CEDEAR para superar la inflación, justificando el riesgo de inversión?”**

El flujo analítico *End-to-End* incluye:

- Ingeniería de Features para la volatilidad (CCL, Ratios).
- Preprocesamiento de Series de Tiempo (Lagging, Normalización).
- Implementación de un modelo **LSTM (Long Short-Term Memory)**.
- **Métricas financieras rigurosas** (RMSE, MAE).
- Despliegue de un prototipo interactivo (MLOps).

---

## 🧠 2. Ingeniería de Features y Análisis Estructural

El proyecto demuestra sólidas habilidades de Ingeniería de Datos en entornos financieros complejos.

### ✔️ Features Clave

- `Precio de Cierre Ajustado` (del CEDEAR).
- `CCL Calculado` (Implícito en la cotización).
- `Volatilidad diaria` (basado en precios históricos).
- `Rendimiento Histórico` vs. `Inflación Mensual`.

### ✔️ Pipeline de Preprocesamiento

El pipeline está diseñado para manejar series de tiempo no estacionarias:

1.  **Imputación:** Uso de `ffill` para manejo inteligente de días sin cotización del CCL.
2.  **Normalización:** Escalamiento de datos para el rendimiento óptimo del modelo LSTM.
3.  **Lagging:** Creación de secuencias de tiempo (ventanas de observación) para la entrada del modelo LSTM.

---

## ⚡ 3. Modelado Predictivo: Deep Learning LSTM

El corazón del proyecto es el modelo LSTM, seleccionado por su capacidad superior para capturar dependencias a largo plazo en datos secuenciales.

| Aspecto | Detalle Técnico |
| :--- | :--- |
| **Modelo** | Red Neuronal Recurrente LSTM (Keras/TensorFlow) |
| **Arquitectura** | [Pendiente: Ej. Capa de entrada, Capa LSTM, Capa Dense] |
| **Validación** | **Time Series Cross-Validation** (Evitando *data leakage*). |
| **Métricas** | **RMSE (Error Cuadrático Medio)** y **MAE (Error Absoluto Medio)** para evaluar la precisión del pronóstico. |

---

## 🔍 4. Interpretación y MLOps (Fase 2)

La transparencia y el despliegue son cruciales para el uso en producción.

### ✔️ Explicabilidad del Modelo (SHAP/LIME)

Se implementará un análisis de **SHAP** o **LIME** para interpretar:
- Cómo factores como la volatilidad o los *lags* de precio afectan el pronóstico.
- La confianza y las variables impulsoras detrás de una señal de compra/venta.

### ✔️ MLOps y Despliegue

Se generará un entregable interactivo con **Streamlit/Plotly Dash** que permita al usuario:
- Seleccionar el *Ticker* (ej. NVDA, TSLA).
- Visualizar el pronóstico del LSTM para los siguientes 7-15 días.

---

## 📁 5. Estructura y Tecnología

### Estructura del Repositorio


cedear\_analysis\_2024/
├── data/
├── scripts/
│   ├── 01\_data\_preprocessing.py        \# Limpieza, CCL y Ratios.
│   ├── 02\_timeseries\_lags.py           \# Ingeniería de features para LSTM.
│   ├── 03\_lstm\_model\_training.py       \# Entrenamiento, tuning y métricas LSTM.
│   └── 04\_streamlit\_deployment.py      \# Despliegue del Dashboard interactivo.
├── models/
├── requirements.txt
└── README.md



### 🧪 Tech Stack

- **Lenguaje:** Python 3.x
- **Librerías ML/DL:** **TensorFlow/Keras** (o PyTorch), Scikit-learn.
- **Data & Finanzas:** Pandas, NumPy, yfinance.
- **Visualización/Deploy:** Matplotlib, Seaborn, **Streamlit** (o Plotly Dash).

---

## 🎯 6. Contacto Profesional

### Cecilia Ledesma

| Credencial | Detalle |
| :--- | :--- |
| **Email** | cecledesma@gmail.com |
| **GitHub** | [https://github.com/ceciagro](https://github.com/ceciagro) |
| **Upwork** | [https://www.upwork.com/freelancers/cledesma](https://www.upwork.com/freelancers/cledesma) |
| **Especializaciones** | Machine Learning, Deep Learning (LSTM), Decision Science, Modelado Financiero, MLOps. |

---

