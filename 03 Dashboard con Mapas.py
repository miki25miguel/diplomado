import streamlit as st
import pandas as pd
import plotly.express as px

import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np

st.title("🗺️ Dashboard con Mapas")

#from pyngrok import ngrok
import time

# Kill any existing ngrok processes aggressively
#!killall ngrok || true # Use '|| true' to prevent script from failing if ngrok isn't running

# Kill any existing ngrok tunnels via pyngrok API
#ngrok.kill()

# Give a small buffer time after killing processes before starting new ones
time.sleep(2)

# Start Streamlit app in the background
#!streamlit run app.py &>/dev/null&

# Wait a bit for Streamlit to start up
time.sleep(5) # A longer delay might be necessary for Streamlit to fully initialize

#public_url = ngrok.connect(8501)
#print(f"Public URL: {public_url}")

#!kill -9 $(lsof -t -i:8501)
