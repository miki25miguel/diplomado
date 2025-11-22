!pip install streamlit pyngrok

from pyngrok import ngrok

ngrok.set_auth_token("35qJAGN9pDjSLGWbj60RqG13IlY_6mpxt5Zix41yDvGyqJ5bX")

%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Dashboard de Ventas")

# Datos de ejemplo
data = {
    "Fecha": pd.date_range("2024-01-01", periods=30),
    "Ventas": [1200,1500,1600,1700,900,800,1800,1950,2000,2200,
               2100,2300,2500,2400,2600,2100,2000,1950,1850,1800,
               1700,1600,1500,1550,1650,1750,1850,1950,2050,2150],
    "Categoria": ["A","B","A","C","B","A","B","C","A","B",
                  "C","C","A","B","B","A","C","A","B","C",
                  "A","B","C","A","B","C","A","B","C","A"]
}
df = pd.DataFrame(data)

categoria = st.selectbox("Selecciona categoría:", df["Categoria"].unique())
df_filtrado = df[df["Categoria"] == categoria]

fig = px.line(df_filtrado, x="Fecha", y="Ventas", title=f"Ventas categoría {categoria}")
st.plotly_chart(fig)

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
