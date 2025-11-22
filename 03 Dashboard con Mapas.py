!pip install streamlit pyngrok

from pyngrok import ngrok
ngrok.set_auth_token("35qJAGN9pDjSLGWbj60RqG13IlY_6mpxt5Zix41yDvGyqJ5bX")

%%writefile app.py
import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("🗺️ Dashboard con Mapas")

# Datos
df = px.data.gapminder().query("year == 2007")[["country", "iso_alpha", "continent"]]
df["valor"] = np.random.randint(10, 100, size=len(df))

fig = px.choropleth(
    df,
    locations="iso_alpha",
    color="valor",
    hover_name="country",
    projection="natural earth",
    title="Mapa Mundial con Valores Aleatorios"
)

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
