import streamlit as st
import pickle
import numpy as np
import pandas as pd
import os

# ── CONFIGURACIÓN ─────────────────────────────────────────
st.set_page_config(
    page_title="Bienestar Equino — Predictor Clínico",
    page_icon="🐴",
    layout="centered"
)

# ── CARGA DE DATOS ────────────────────────────────────────
@st.cache_data
def cargar_datos():
    try:
        ruta = os.path.join('data', 'horse_limpio.csv')
        df = pd.read_csv(ruta)
        return df
    except Exception as e:
        st.error(f"Error cargando datos: {e}")
        return None

df = cargar_datos()

# ── CARGA DE MODELOS ──────────────────────────────────────
@st.cache_resource
def cargar_modelos():
    try:
        ruta_modelo = os.path.join("models", "modelo_equino.pkl")
        ruta_scaler = os.path.join("models", "scaler_equino.pkl")
        ruta_le     = os.path.join("models", "label_encoder.pkl")
        ruta_feat   = os.path.join("models", "features.pkl")

        with open(ruta_modelo, 'rb') as f:
            modelo = pickle.load(f)
        with open(ruta_scaler, 'rb') as f:
            scaler = pickle.load(f)
        with open(ruta_le, 'rb') as f:
            le = pickle.load(f)
        with open(ruta_feat, 'rb') as f:
            features = pickle.load(f)

        return modelo, scaler, le, features

    except Exception as e:
        st.error(f"Error cargando modelos: {e}")
        return None, None, None, None

modelo, scaler, le, features = cargar_modelos()

if modelo is None:
    st.stop()

# ── ENCABEZADO ────────────────────────────────────────────
st.title("🐴 Predictor de Bienestar Equino")
st.subheader("Herramienta de apoyo clínico veterinario")

st.info("Complete los datos clínicos y presione 'Analizar caballo'")

st.warning("""
⚠️ Esta herramienta es un apoyo basado en Machine Learning.
No reemplaza el diagnóstico veterinario profesional.
""")

st.divider()

# ── FORMULARIO ────────────────────────────────────────────
st.header("📋 Datos clínicos del caballo")

col1, col2 = st.columns(2)

with col1:
    age = st.selectbox("Edad", [0, 1],
        format_func=lambda x: "Adulto" if x == 0 else "Joven")

    pulse = st.slider("Pulso (ppm)", 30, 184, 60)

    rectal_temp = st.slider("Temperatura (°C)", 35.0, 41.0, 38.2, 0.1)

    respiratory_rate = st.slider("Frecuencia respiratoria", 8, 96, 20)

    surgery = st.selectbox("¿Cirugía?", [0, 1],
        format_func=lambda x: "No" if x == 0 else "Sí")

with col2:
    pain = st.selectbox("Dolor", [0,1,2,3,4])

    peristalsis = st.selectbox("Peristalsis", [0,1,2,3])

    packed_cell_volume = st.slider("Volumen celular (%)", 23, 75, 45)

    total_protein = st.slider("Proteína total", 3.0, 89.0, 7.5, 0.1)

    abdominal_distention = st.selectbox("Distensión abdominal", [0,1,2,3])

st.divider()

# ── FUNCIONES ─────────────────────────────────────────────
def calcular_bienestar(pulse, rectal_temp, pain, peristalsis):
    score = 0

    if pulse <= 44: score += 3
    elif pulse <= 60: score += 2
    elif pulse <= 80: score += 1

    if 37.5 <= rectal_temp <= 38.5: score += 2
    elif 37.0 <= rectal_temp <= 39.0: score += 1

    if pain == 0: score += 3
    elif pain == 1: score += 2
    elif pain == 2: score += 1

    if peristalsis == 2: score += 2
    elif peristalsis == 1: score += 1

    return score

def nivel_bienestar(score):
    if score >= 8: return "Alto", "🟢"
    elif score >= 5: return "Moderado", "🟡"
    elif score >= 2: return "Bajo", "🟠"
    else: return "Crítico", "🔴"

# ── PREDICCIÓN ────────────────────────────────────────────
if st.button("🔍 Analizar caballo", use_container_width=True):

    entrada = {f: 0 for f in features}

    entrada.update({
        'age': age,
        'pulse': pulse,
        'rectal_temp': rectal_temp,
        'respiratory_rate': respiratory_rate,
        'surgery': surgery,
        'pain': pain,
        'peristalsis': peristalsis,
        'packed_cell_volume': packed_cell_volume,
        'total_protein': total_protein,
        'abdominal_distention': abdominal_distention
    })

    idx = calcular_bienestar(pulse, rectal_temp, pain, peristalsis)
    entrada['indice_bienestar'] = idx

    try:
        X = pd.DataFrame([entrada])[features]
        X_scaled = scaler.transform(X)

        pred = modelo.predict(X_scaled)
        proba = modelo.predict_proba(X_scaled)[0]
        resultado = le.inverse_transform(pred.astype(int))[0]

        nivel, emoji = nivel_bienestar(idx)

        st.divider()
        st.header("📊 Resultado")

        if resultado == 'lived':
            st.success("✅ SOBREVIVE")
        elif resultado == 'died':
            st.error("❌ ALTO RIESGO")
        else:
            st.warning("⚠️ EUTANASIA")

        st.subheader("Probabilidades")
        for clase, p in zip(le.classes_, proba):
            st.write(f"{clase}: {p*100:.1f}%")

        st.subheader("Bienestar")
        st.metric("Índice", f"{idx}/9")
        st.metric("Nivel", f"{emoji} {nivel}")
        st.progress(idx / 9)

    except Exception as e:
        st.error(f"Error en predicción: {e}")