# 🐴 Predictor de Bienestar Equino
## Herramienta de apoyo veterinario basada en Machine Learning

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML-green)
![Estado](https://img.shields.io/badge/Estado-Activo-brightgreen)

---

## 📌 Descripción

Aplicación web interactiva que predice la probabilidad de
supervivencia de un caballo basándose en sus indicadores
clínicos, usando un modelo de Machine Learning entrenado
con datos reales.

> *"Los datos clínicos cuentan una historia de sufrimiento
> o bienestar antes de que cualquier diagnóstico sea evidente."*

---

## 🚀 App en vivo

👉 **[Probar la app aquí](https://bienestarequino-george-1902.streamlit.app/)**

---

## 🎯 ¿Qué hace esta app?

El veterinario ingresa los datos clínicos del caballo:
- Pulso, temperatura, frecuencia respiratoria
- Nivel de dolor, peristalsis
- Volumen celular, proteína total
- Edad, distensión abdominal

Y el modelo responde en segundos:
- ✅ **SOBREVIVIRÁ** — con probabilidad estimada
- ❌ **ALTO RIESGO DE MUERTE** — con alertas clínicas
- ⚠️ **CONSIDERAR EUTANASIA** — con indicadores críticos

---

## 🏥 Índice de Bienestar Equino

La app calcula un índice propio **(0–9)** en tiempo real:

| Nivel | Rango | Tasa de Supervivencia |
|-------|-------|-----------------------|
| 🟢 Alto | 8–9 | 60% |
| 🟡 Moderado | 5–7 | 79% |
| 🟠 Bajo | 2–4 | 45% |
| 🔴 Crítico | 0–1 | 18% |

---

## 🤖 Modelo de Machine Learning

- **Algoritmo:** Random Forest optimizado con GridSearchCV
- **Clases:** Lived, Died, Euthanized
- **Dataset:** 299 caballos — Horse Survival Dataset (Kaggle)
- **F1-macro:** 0.5023

| Clase | Precision | Recall | F1-Score |
|-------|-----------|--------|----------|
| Lived | 0.69 | 0.69 | 0.69 |
| Died | 0.53 | 0.60 | 0.56 |
| Euthanized | 0.29 | 0.22 | 0.25 |

---

## ⚠️ Alertas clínicas automáticas

La app detecta y muestra alertas en tiempo real:

- 🔴 Pulso muy elevado — estrés cardiovascular severo
- 🔴 Temperatura anormal — posible infección o hipotermia
- 🔴 Dolor severo — requiere atención inmediata
- 🔴 Peristalsis ausente — riesgo de cólico
- 🟡 Proteína elevada — posible deshidratación

---

## 💼 Aplicación práctica

Esta herramienta puede ser utilizada en:

- Clínicas veterinarias equinas
- Centros ecuestres y haras
- Servicios de emergencia veterinaria
- Formación de veterinarios junior

---

## 🛠️ Tecnologías utilizadas

- **Python 3.12**
- **Streamlit** — interfaz web interactiva
- **Scikit-learn** — Random Forest, GridSearchCV
- **Pandas / NumPy** — procesamiento de datos
- **Pickle** — serialización del modelo
- **Streamlit Cloud** — despliegue gratuito

---

## 📁 Estructura del repositorio
```
bienestar_equino_app/
│
├── models/
│   ├── modelo_equino.pkl
│   ├── scaler_equino.pkl
│   ├── label_encoder.pkl
│   └── features.pkl
│
├── app.py
├── README.md
└── requirements.txt
```

---

## 🔗 Repositorio del análisis completo

Este repositorio contiene solo la app. Para ver el análisis
completo con EDA, visualizaciones y desarrollo del modelo:

👉 [Ver análisis completo](https://github.com/George1902/bienestar_equino)

---

## 🚀 Cómo ejecutar localmente
```bash
git clone https://github.com/George1902/bienestar_equino_app.git
cd bienestar_equino_app
pip install -r requirements.txt
streamlit run app.py
```

---

## 📊 Fuente de datos

**Horse Survival Dataset**
Kaggle — Yasser H
🔗 https://www.kaggle.com/datasets/yasserh/horse-survival-dataset

---

## 👨‍💻 Autor

**Jorge Ojeda**
Estudiante de Ciencia de Datos
Oracle Next Education (ONE) — Alura LATAM
📅 2026

---

## ⚠️ Aviso importante

Esta herramienta es un apoyo clínico basado en Machine
Learning con 65% de accuracy. **No reemplaza el diagnóstico
veterinario profesional.**

---

## 📄 Licencia

Proyecto de uso educativo y libre distribución.
