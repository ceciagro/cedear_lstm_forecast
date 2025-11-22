<p align="center">
  <img src="assets/banner_cedear_forecast.jpg" alt="CEDEARs LSTM Forecast Banner" width="100%">
</p>

# 💰 Precios y Rendimientos de CEDEARs: Deep Learning (LSTM) para Estrategia Financiera

**Author:** Cecilia Ledesma  
**GitHub:** https://github.com/ceciagro  
**Role:** Data Scientist – Portfolio Project: Advanced Time Series

---
## 🔗 Dataset Source & Context / *Source and Context*

Este proyecto utiliza precios históricos de acciones y datos del mercado financiero argentino para generar la base de predicción.

- **Fuente de Precios:** **Yahoo Finance** (vía `yfinance`). / *Price Source: Yahoo Finance.*
- **Datos Secundarios:** Cotizaciones del tipo de cambio **Contado con Liquidación (CCL)** y datos de inflación histórica. / *Secondary Data: CCL exchange rate and historical inflation.*
- **Contexto:** Enfoque en la volatilidad de los CEDEARs en pesos argentinos y su rendimiento ajustado por inflación. / *Context: Focus on CEDEAR volatility and inflation-adjusted return.*

---
## 🚀 1. Project Overview: De la Historia al Pronóstico / *From History to Forecast*

El objetivo central es: **“¿Cómo se puede pronosticar el rendimiento real de un CEDEAR para superar la inflación, justificando el riesgo de inversión?”**

El flujo analítico *End-to-End* incluye: Ingeniería de Features (CCL, Ratios), Preprocesamiento de Series de Tiempo (**Lagging**, **Normalización**), Implementación de un modelo **LSTM** (Long Short-Term Memory), **Métricas financieras rigurosas** (RMSE, MAE), y Despliegue interactivo (**MLOps**).

---
## 🧠 2. Ingeniería de Features y Análisis Estructural / *Feature Engineering and Structural Analysis*

El proyecto demuestra sólidas habilidades de **Ingeniería de Datos** en entornos financieros complejos. / *The project demonstrates solid **Data Engineering** skills in complex financial environments.*

### ✔️ Features Clave / *Key Features*

- `Precio de Cierre Ajustado` (del CEDEAR) / *`Adjusted Closing Price` (of the CEDEAR).*
- `CCL Calculado` (Implícito en la cotización) / *`Calculated CCL` (Implied in the quote).*
- `Volatilidad diaria` (basado en precios históricos) / *`Daily Volatility` (based on historical prices).*
- `Rendimiento Histórico` vs. `Inflación Mensual` / *`Historical Return` vs. `Monthly Inflation`.*

### ✔️ Pipeline de Preprocesamiento / *Preprocessing Pipeline*

El pipeline está diseñado para manejar series de tiempo no estacionarias: / *The pipeline is designed to handle non-stationary time series:*

1.  **Imputación:** Uso de `ffill` para manejo inteligente de días sin cotización del CCL. / *Imputation: Use of `ffill` for intelligent handling of days without CCL quotation.*
2.  **Normalización:** Escalamiento de datos para el rendimiento óptimo del modelo LSTM. / *Normalization: Data scaling for optimal LSTM model performance.*
3.  **Lagging:** Creación de secuencias de tiempo (ventanas de observación) para la entrada del modelo LSTM. / *Lagging: Creation of time sequences (observation windows) for the LSTM model input.*

---
## ⚡ 3. Modelado Predictivo: Deep Learning LSTM / *Predictive Modeling*

| Aspecto / *Aspect* | Detalle Técnico / *Technical Detail* |
| :--- | :--- |
| **Modelo** / *Model* | Red Neuronal Recurrente **LSTM** (Keras/TensorFlow) |
| **Validación** / *Validation* | **Time Series Cross-Validation** (Evitando *data leakage*). |
| **Métricas** / *Metrics* | **RMSE** (Error Cuadrático Medio) y **MAE** (Error Absoluto Medio). |

---
## 🔍 4. Interpretación y MLOps / *Interpretation and MLOps*

### ✔️ Explicabilidad del Modelo (SHAP/LIME)

Se implementará un análisis de **SHAP** o **LIME** para interpretar el impacto de las *features* en el pronóstico. / *SHAP/LIME analysis will be implemented to interpret feature impact on the forecast.*

### ✔️ MLOps y Despliegue Interactivo (Streamlit)

| Componente / *Component* | Función para el Usuario / *User Function (Business Value)* |
| :--- | :--- |
| **Selector de Ticker** / *Ticker Selector* | Permite al usuario seleccionar el CEDEAR de interés para generar un pronóstico a medida. / *Allows the user to select the CEDEAR for custom forecast generation.* |
| **Gráfico de Pronóstico** / *Forecast Plot* | Muestra el precio histórico y superpone la curva de predicción del LSTM a 7 o 15 días. / *Displays historical price and overlays the LSTM's 7-15 day prediction curve.* |
| **Métricas Clave (RMSE/MAE)** / *Key Metrics (RMSE/MAE)* | Valida la fiabilidad del pronóstico mostrando la precisión del modelo en la interfaz. / *Validates forecast reliability by displaying model accuracy on the interface.* |

---
## 📁 5. Estructura y Tecnología / *Structure and Technology*

### 📜 Desglose de Scripts / *Scripts Breakdown*

| Archivo / *File* | Responsabilidad Granular / *Granular Responsibility* |
| :--- | :--- |
| **`01_data_preprocessing.py`** | **Extracción y Limpieza:** Descarga precios, calcula CCL y features. / *Data Extraction, Cleaning, and Feature Calculation (CCL, Ratios).* |
| **`02_timeseries_lags.py`** | **Ingeniería de Features Avanzada:** Crea secuencias de *lags* y aplica normalización para LSTM. / *Advanced Feature Engineering: Creates lag sequences and applies normalization for LSTM input.* |
| **`03_lstm_model_training.py`** | **Modelado y Evaluación:** Define la arquitectura LSTM, entrena, implementa **Validación Cruzada de Series de Tiempo** y guarda métricas. / *Modeling & Evaluation: Defines LSTM architecture, trains, implements **Time Series Cross-Validation**, and saves metrics.* |
| **`04_streamlit_deployment.py`** | **Despliegue Interactivo (MLOps):** Lógica del Dashboard. Carga el modelo y genera la interfaz de visualización. / *Interactive Deployment (MLOps): Dashboard Logic. Loads model and generates the visualization interface.* |

### 🧪 Tech Stack

- **Lenguaje / *Language*:** Python 3.x
- **Librerías ML/DL:** **TensorFlow/Keras** (o PyTorch), Scikit-learn.
- **Data & Finanzas:** Pandas, NumPy, yfinance.
- **Visualización/Deploy:** Matplotlib, Seaborn, **Streamlit** (o Plotly Dash).

---
## 🎯 6. Contacto Profesional / *Professional Contact*

| Credencial / *Credential* | Detalle / *Detail* |
| :--- | :--- |
| **Author** | **Cecilia Ledesma** |
| **Email** | cecledesma@gmail.com |
| **GitHub** | [https://github.com/ceciagro](https://github.com/ceciagro) |
| **Upwork** | [https://www.upwork.com/freelancers/cledesma](https://www.upwork.com/freelancers/cledesma) |
| **Especializaciones** | Deep Learning (LSTM), Time Series Forecasting, Financial Modeling, MLOps. |

---
