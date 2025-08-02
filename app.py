import streamlit as st
import requests
import pandas as pd
from datetime import datetime

url = "https://taxifare.lewagon.ai/predict"

st.title("🚕 Taxi Fare Predictor")

# 1. Date et heure
pickup_date = st.date_input("Date de prise en charge", value=datetime.today())
pickup_time = st.time_input("Heure de prise en charge", value=datetime.now().time())

# 2. Coordonnées
lon_start = st.number_input("Longitude départ", value=-73.95, format="%.6f")
lat_start = st.number_input("Latitude départ", value=40.78, format="%.6f")
lon_end   = st.number_input("Longitude arrivée", value=-73.98, format="%.6f")
lat_end   = st.number_input("Latitude arrivée", value=40.77, format="%.6f")

# 3. Nombre de passagers
passengers = st.slider("Nombre de passagers", 1, 8, 1)

if st.button("🧠 Prédire le prix"):
    pickup_datetime = datetime.combine(pickup_date, pickup_time).isoformat()

    payload = {
        "pickup_datetime": pickup_datetime,
        "pickup_longitude": lon_start,
        "pickup_latitude": lat_start,
        "dropoff_longitude": lon_end,
        "dropoff_latitude": lat_end,
        "passenger_count": passengers
    }

    url = "https://taxifare.lewagon.ai/predict"

    response = requests.get(url, params=payload)

df = pd.DataFrame({
    "lat": [lat_start, lat_end],
    "lon": [lon_start, lon_end]
})
st.map(df)

'''
# TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
