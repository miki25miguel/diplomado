!pip install streamlit pyngrok

from pyngrok import ngrok

ngrok.set_auth_token("35qJAGN9pDjSLGWbj60RqG13IlY_6mpxt5Zix41yDvGyqJ5bX")

%%writefile app.py
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.title("📊 Dashboard Interactivo con Widgets")

# -----------------------------
# Datos de ejemplo
# -----------------------------
np.random.seed(42)
dates = pd.date_range("2024-01-01", periods=100)
df = pd.DataFrame({
    "fecha": dates,
    "ventas": np.random.randint(1000, 5000, size=100),
    "categoria": np.random.choice(["A", "B", "C"], size=100),
    "tienda": np.random.choice(["Norte", "Sur", "Este", "Oeste"], size=100)
})

# -----------------------------
# SIDEBAR: WIDGETS
# -----------------------------
st.sidebar.header("Filtros del Dashboard")

# 1) Selección de categoría
categoria = st.sidebar.selectbox(
    "Selecciona una categoría",
    options=df["categoria"].unique()
)

# 2) Rango de fechas
fecha_inicio = st.sidebar.date_input("Fecha inicial", df["fecha"].min())
fecha_fin = st.sidebar.date_input("Fecha final", df["fecha"].max())

# 3) Checkbox para activar un filtro adicional
activar_tienda = st.sidebar.checkbox("Filtrar por tienda")

if activar_tienda:
    tienda = st.sidebar.selectbox(
        "Selecciona la tienda",
        options=df["tienda"].unique()
    )

# 4) Slider de rango de ventas
rango_ventas = st.sidebar.slider(
    "Rango mínimo de ventas",
    min_value=1000,
    max_value=5000,
    value=2000
)

# 5) Botón para aplicar filtros
aplicar = st.sidebar.button("Aplicar filtros")

# -----------------------------
# APLICAR LOS FILTROS
# -----------------------------
df_filtrado = df.copy()

if aplicar:
    df_filtrado = df_filtrado[df_filtrado["categoria"] == categoria]
    df_filtrado = df_filtrado[(df_filtrado["fecha"] >= pd.to_datetime(fecha_inicio)) &
                              (df_filtrado["fecha"] <= pd.to_datetime(fecha_fin))]
    df_filtrado = df_filtrado[df_filtrado["ventas"] >= rango_ventas]

    if activar_tienda:
        df_filtrado = df_filtrado[df_filtrado["tienda"] == tienda]


# -----------------------------
# MOSTRAR DATOS Y GRÁFICAS
# -----------------------------
st.subheader("📄 Datos Filtrados")
st.dataframe(df_filtrado)

st.subheader("📈 Ventas filtradas en el tiempo")
fig = px.line(df_filtrado, x="fecha", y="ventas", markers=True)
st.plotly_chart(fig)

st.subheader("🛍️ Ventas por Categoría")
fig_bar = px.bar(df_filtrado, x="categoria", y="ventas")
st.plotly_chart(fig_bar)

from pyngrok import ngrok
import time

# Kill any existing ngrok processes aggressively
!killall ngrok || true # Use '|| true' to prevent script from failing if ngrok isn't running

# Kill any existing ngrok tunnels via pyngrok API
ngrok.kill()

# Give a small buffer time after killing processes before starting new ones
time.sleep(2)

# Start Streamlit app in the background
!streamlit run app.py &>/dev/null&

# Wait a bit for Streamlit to start up
time.sleep(5) # A longer delay might be necessary for Streamlit to fully initialize

public_url = ngrok.connect(8501)
print(f"Public URL: {public_url}")

#!kill -9 $(lsof -t -i:8501)
