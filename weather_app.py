import streamlit as st
import requests

# Function to get weather data from wttr.in
def get_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        else:
            return None
    except:
        return None

# Function to display weather
def show_weather(data, city):
    current = data['current_condition'][0]
    st.subheader(f"📍 Weather in {city.title()}")
    st.metric("🌡️ Temperature (°C)", current["temp_C"])
    st.metric("💧 Humidity (%)", current["humidity"])
    st.metric("🌬️ Wind Speed (km/h)", current["windspeedKmph"])
    st.write(f"🌥️ Condition: **{current['weatherDesc'][0]['value']}**")

# Streamlit UI
def main():
    st.set_page_config(page_title="Weather App", page_icon="🌦️")
    st.title("🌦️ Real-Time Weather App (No API Key)")
    st.write("Get real-time weather updates using **wttr.in**")

    city = st.text_input("Enter City Name", "Pune")

    if st.button("Get Weather"):
        data = get_weather_data(city)
        if data:
            show_weather(data, city)
        else:
            st.error("❌ Could not fetch weather data. Check the city name or internet connection.")

if __name__ == "__main__":
    main()
