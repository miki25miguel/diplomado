!pip install streamlit pyngrok

from pyngrok import ngrok

ngrok.set_auth_token("35qJAGN9pDjSLGWbj60RqG13IlY_6mpxt5Zix41yDvGyqJ5bX")


# Define the Streamlit app content and save it to app.py
streamlit_app_content = """
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import plotly.express as px

st.title("🤖 Dashboard de Machine Learning")

# Datos sintéticos
X = np.arange(1, 21).reshape(-1,1)
y = 3 * X.flatten() + 10

model = LinearRegression()
model.fit(X, y)

# Gráfica
df = pd.DataFrame({"X": X.flatten(), "y": y})
fig = px.scatter(df, x="X", y="y", trendline="ols", title="Datos y modelo")
st.plotly_chart(fig)

# Predicción
valor = st.number_input("Ingresa valor X para predecir:", min_value=0.0)
pred = model.predict([[valor]])[0]

st.success(f"Predicción del modelo: {pred:.2f}")
"""

with open("app.py", "w") as f:
    f.write(streamlit_app_content)

print("app.py created successfully.")

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
