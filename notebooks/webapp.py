# Import libraries
import streamlit as st
import pandas as pd
import xgboost as xgb
import requests
import pickle
from pathlib import Path
from config import MAPQUEST_API_KEY, WALKSCORE_API_KEY


# Write the title for web app
st.write("# Rental Price Prediction in Kelowna")

Type = st.selectbox("Enter type of rental property",["Room", "Apartment/Condo", "House", "Townhouse"])

# Show boxes in 3 columns
col1, col2, col3 = st.columns(3)

n_beds = col1.number_input("Enter number of beds")
n_bath = col2.number_input("Enter number of bathrooms")
Area = col3.number_input("Enter area of the property")
laundry = col1.selectbox("Select laundry type",["In-unit", "In building", "Available"])
heating = col2.selectbox("Select heating type",["Central", "Electric", "Gas", "Radiator", "Available"])
city = col3.selectbox("Choose your city", ['kelowna', 'west kelowna', 'vernon', 'peachland', 'central okanagan', 'lake country', 'penticton', 'okanagan-similkameen', 'lumby', 'kootenay boundary', 'north okanagan', 'summerland', 'coldstream', 'spallumcheen'])
postal_code = col1.text_input("Enter your postal code")

# In model these parameters are boolean
if Type == "Apartment/Condo":
    Type = 1
else:
    Type = 0

if laundry == "In-unit":
    laundry = 1
else:
    laundry = 0

if heating == "Central":
    heating = 1
else:
    heating = 0

def get_location_scores(city, postal_code):
    """
Get the latitude, longitude, walk score, and bike score of a given location.

Args:
    city (str): The name of the city.
    postal_code (str): The postal code of the city.

Returns:
    Dict[str, float]: A dictionary containing the latitude, longitude, walk score, and bike score of the location.
"""
    # get latitude and longitude using MapQuest API
    api_key = MAPQUEST_API_KEY
    address = f"{city}, {postal_code}"
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={address}"
    response = requests.get(url)
    data = response.json()
    lat = data["results"][0]["locations"][0]["latLng"]["lat"]
    lng = data["results"][0]["locations"][0]["latLng"]["lng"]

    # get walk score, bike score, and transit score using Walk Score API
    api_key = WALKSCORE_API_KEY
    url = f"https://api.walkscore.com/score?format=json&address={address}&lat={lat}&lon={lng}&transit=1&bike=1&wsapikey={api_key}"
    response = requests.get(url)
    data = response.json()
    walk_score = data.get("walkscore", -1)
    bike_score = data.get("bike", {}).get("score", -1)
    j
    # return a dictionary containing the location scores
    return {'Bike Score': bike_score, 'Walk Score': walk_score, 'lng': lng, 'lat': lat}

# get location scores
location_scores = get_location_scores(city, postal_code)

data = {
    'nbeds': [n_beds],
    'Area': [Area],
    'Type_Apartment/Condo': [Type],
    'nbath': [n_bath],
    **location_scores,
    'laundry_in-unit laundry': [laundry],
    'heating_central heating': [heating],
}
df = pd.DataFrame(data)

path = Path(__file__).parent / "fhs_xgb_model.pkl"

with open(path, 'rb') as file:
    fhs_xgb_model = pickle.load(file)

# Make prediction
prediction = fhs_xgb_model.predict(xgb.DMatrix(df))

if st.button('Predict'):
    st.write(f"Predicted rental price: ${prediction[0]:,.0f} per month")


