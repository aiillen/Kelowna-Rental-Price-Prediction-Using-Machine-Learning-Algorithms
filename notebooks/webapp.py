import streamlit as st
import pandas as pd
import xgboost as xgb
import requests
import joblib


st.write("# Rental Price Prediction in Kelowna")

Type = st.selectbox("Enter type of rental property",["Room", "Apartment/Condo", "House", "Townhouse"])

col1, col2, col3 = st.columns(3)

n_beds = col1.number_input("Enter number of beds")
n_bath = col2.number_input("Enter number of bathrooms")
Area = col3.number_input("Enter area of the property")

laundry = col1.selectbox("Select laundry type",["In-unit", "In building", "Available"])
heating = col2.selectbox("Select heating type",["Central", "Electric", "Gas", "Radiator", "Available"])

city = col3.selectbox("Choose your city", ['kelowna', 'west kelowna', 'vernon', 'peachland', 'central okanagan', 'lake country', 'penticton', 'okanagan-similkameen', 'lumby', 'kootenay boundary', 'north okanagan', 'summerland', 'coldstream', 'spallumcheen'])

postal_code = col1.text_input("Enter your postal code")


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
    # get latitude and longitude using MapQuest API
    api_key = "ojSeJRAYm07WLKZhHKRbxXdXTiXmF6o2"
    address = f"{city}, {postal_code}"
    url = f"http://www.mapquestapi.com/geocoding/v1/address?key={api_key}&location={address}"
    response = requests.get(url)
    data = response.json()
    lat = data["results"][0]["locations"][0]["latLng"]["lat"]
    lng = data["results"][0]["locations"][0]["latLng"]["lng"]

    # get walk score, bike score, and transit score using Walk Score API
    api_key = "77cae2ef1955f6efd33b4f873891dd75"
    url = f"https://api.walkscore.com/score?format=json&address={address}&lat={lat}&lon={lng}&transit=1&bike=1&wsapikey={api_key}"
    response = requests.get(url)
    data = response.json()
    walk_score = data.get("walkscore", -1)
    bike_score = data.get("bike", {}).get("score", -1)

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

# Load the trained model
model = joblib.load("fhs_xgb_model.pkl")

# Make prediction
prediction = model.predict(xgb.DMatrix(df))

if st.button('Predict'):
    st.write(f"Predicted rental price: ${prediction[0]:,.0f} per month")


# Output the predicted price
