import requests
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from datetime import datetime, timedelta

# Function to get coordinates from Nominatim
def get_coordinates(city_name):
    url = f"https://nominatim.openstreetmap.org/search?q={city_name}&format=json&limit=1"
    response = requests.get(url)
    if response.status_code == 200:
        location_data = response.json()
        if location_data:
            return float(location_data[0]['lat']), float(location_data[0]['lon'])
    return None, None

# Function to get weather data from Open-Meteo
def get_weather_data(lat, lon):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    return None

# Function to get historical weather data
def get_historical_weather(lat, lon, days=7):
    historical_data = []
    for i in range(days):
        date = (datetime.now() - timedelta(days=i)).strftime('%Y-%m-%d')
        url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&daily=temperature_2m_max,temperature_2m_min&timezone=auto&start={date}&end={date}"
        response = requests.get(url)
        if response.status_code == 200:
            historical_data.append(response.json())
    return historical_data

# Streamlit app
st.title("GeoWeather Insights 🌤️")

# User authentication (simple)
if 'username' not in st.session_state:
    st.session_state.username = None

if st.session_state.username is None:
    st.subheader("User  Authentication")
    username = st.text_input("Enter Username")
    if st.button("Login"):
        if username:
            st.session_state.username = username
            st.success(f"Welcome, {username}!")
        else:
            st.error("Please enter a username.")
else:
    st.subheader(f"Welcome back, {st.session_state.username}!")

    city_name = st.text_input("Enter City Name", value="San Francisco")

    if st.button("Get Weather Data"):
        lat, lon = get_coordinates(city_name)
        if lat and lon:
            st.write(f"Coordinates: Latitude: {lat}, Longitude: {lon}")
            data = get_weather_data(lat, lon)
            if data:
                # Display current weather data
                st.subheader("Current Weather Data")
                current_weather = data['hourly']
                temperature = current_weather['temperature_2m']
                humidity = current_weather['relative_humidity_2m']
                wind_speed = current_weather['wind_speed_10m']
                time = current_weather['time']

                # Create a DataFrame for visualization
                df = pd.DataFrame({
                    'Time': pd.to_datetime(time),
                    'Temperature (°C)': temperature,
                    'Humidity (%)': humidity,
                    'Wind Speed (m/s)': wind_speed
                })

                # Display the DataFrame
                st.write(df)

                # Plotting current weather data
                fig, ax1 = plt.subplots(figsize=(10, 5))

                # Plot temperature
                ax1.set_xlabel('Time')
                ax1.set_ylabel('Temperature (°C)', color='tab:red')
                ax1.plot(df['Time'], df['Temperature (°C)'], color='tab:red', label='Temperature (°C)')
                ax1.tick_params(axis='y', labelcolor='tab:red')

                # Create a second y-axis for humidity
                ax2 = ax1.twinx()
                ax2.set_ylabel('Humidity (%)', color='tab:blue')
                ax2.plot(df['Time'], df['Humidity (%)'], color='tab:blue', label='Humidity (%)')
                ax2.tick_params(axis='y', labelcolor='tab:blue')

                # Show the plot
                fig.tight_layout()
                st.pyplot(fig)

                # Historical Weather Data
                st.subheader("Historical Weather Data (Last 7 Days)")
                historical_data = get_historical_weather(lat, lon)
                if historical_data:
                    historical_temps_max = []
                    historical_temps_min = []
                    historical_dates = []
                    for day_data in historical_data:
                        daily_data = day_data['daily']
                        historical_dates.append(daily_data['time'][0])
                        historical