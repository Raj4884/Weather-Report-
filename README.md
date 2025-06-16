🌦️ Real-Time Weather Report App (No API Key)
A simple yet powerful Streamlit web application that fetches real-time weather data using wttr.in — no API key required. This project demonstrates your Python skills, real-time data integration, and frontend building using Streamlit — perfect for showcasing in internships or portfolios.

📌 Features
🔄 Real-time weather updates

✅ No API key required

🌐 Fetches data using wttr.in

📊 Clean and interactive Streamlit interface

🌡️ Displays:

Temperature

Humidity

Wind Speed

Weather condition

📁 Project Structure
rust
Copy code
📦 Weather
├── weather_streamlit_no_api.py   ← Streamlit App
├── requirements.txt              ← Project Dependencies
└── README.md                     ← You're reading it!
📦 Requirements
txt
Copy code
streamlit
requests
Install all dependencies with:

bash
Copy code
pip install -r requirements.txt
🚀 How to Run
bash
Copy code
streamlit run weather_streamlit_no_api.py

💡 Code Preview
python
Copy code
def get_weather_data(city):
    url = f"https://wttr.in/{city}?format=j1"
    response = requests.get(url)
    return response.json()
    
📌 Why This Project?
It shows your grasp of:

Python scripting

Streamlit frontend building

JSON parsing

User input handling

Live data integration
