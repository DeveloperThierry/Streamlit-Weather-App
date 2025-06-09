import streamlit as st
import pandas as pd
import numpy as np
import requests 

import os
from dotenv import load_dotenv

# load_dotenv()

API_KEY = st.secrets["API_KEY"]

def set_custom_widget_color(user_color):
  st.markdown(f"""
  <style>
    .stApp {{
            color: {user_color};
        }}
  </style>
  """, True)

def get_current_weather(city, unit="metric"):
  url =  f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units={unit}"
  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    return None

def extract_weather_data(data):
  weather = {
    "City":data["name"],
    "Temperature": data["main"]["temp"],
    "Humidity": data["main"]["humidity"],
    "Pressure":data["main"]["pressure"],
    "Wind Speed (m/s)": data["wind"]["speed"],
    "Condition": data["weather"][0]["description"].title(),
    "Lat":data["coord"]["lat"],
    "Lon": data["coord"]["lon"]
  }
  return weather


st.set_page_config(page_title=" My Weather App", page_icon="🌤️", layout="wide")
st.title("🌦️ My Real-Time Weather Dashboard")
st.subheader("Check the forecast in your city")
st.caption("Powered by OpenWeatherMap API")
user_color = st.color_picker("Change text color", "#FFFFFF")
set_custom_widget_color(user_color)
st.markdown("---")


st.header(" 🔍 Search Weather")
city = st.text_input("Enter a city name", placeholder="Miami")
unit = st.radio("Select units", options=["Celsius", "Fahrenheit"])
unit_format = "metric" if "Celsius" in unit else "imperial"
days = st.slider("Select number of forecast days", min_value=1, max_value=5, value=3)
show_more = st.checkbox("Select to show chart for (humidity, wind, etc.) ")


if st.button("Get Weather"):
  if city.strip() == "":
    st.warning("⚠️ City name is missing. Please enter city name. (ex. Miami)")
  else:
    st.info(" ⏳ loading weather data...")
    
    data = get_current_weather(city, unit_format)
    if data:
      weather_info = extract_weather_data(data)
      basic_info = {
        "City":weather_info["City"],
        "Temperature":weather_info["Temperature"],
        "Condition":weather_info["Condition"]
      }
      basic_df = pd.DataFrame([basic_info])
      st.success(f"✅ Weather data successfully loaded for {weather_info['City']}")
      st.subheader("🌡️ Basic Weather Information")
      st.dataframe(basic_df)

      if show_more:
        st.subheader("🌡️ Advanced Weather Information")
        st.info("More Detailed Weather Forecasts")
        df = pd.DataFrame([weather_info])
        st.dataframe(df)


        st.info("Showing more details: humidity, pressure, and wind speed")
        added_data = pd.DataFrame({
          "Metric":["Humidity", "Pressure", "Wind Speed"],
          "Value": [
            weather_info["Humidity"],
            weather_info["Pressure"],
            weather_info["Wind Speed (m/s)"]
          ]

        }).set_index("Metric")
        st.bar_chart(added_data)
      
      st.subheader("📊 Forecasts & Visualizations")
      st.info("Temperature Line Graph") 
      temps = [weather_info["Temperature"] + i for i in range(days)]
      days_range = [f"Day {i+1}" for i in range(days)]
      forecast_df = pd.DataFrame({
        "Day":days_range,
        "Temperature":temps
      }).set_index("Day")
      st.line_chart(forecast_df)
      
      st.subheader("🗺️ Location Map")
      location_df = pd.DataFrame({
        'lat':[weather_info["Lat"]],
        'lon':[weather_info["Lon"]]
      })

      st.map(location_df)

    else:
      st.error(" ❌  Failed to load data. Please check city name.")

st.markdown("---")

st.caption("Project 2 - UI/UX Design with Streamlit  @Thierry Laguerre")
