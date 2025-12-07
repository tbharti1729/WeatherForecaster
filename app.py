import streamlit as st
import pandas as pd
from weather.weather_fetcher import get_weather, get_forecast, load_history

# ---- PAGE CONFIG ----
st.set_page_config(page_title="🌦️ Weather Forecaster", layout="wide")

# ---- DARK THEME + COHESIVE COLORS ----
st.markdown("""
<style>
/* App background */
.stApp {
    background-color: #1e1e2f;
    color: white;
}

/* Main title */
.title {
    color: #00d4ff;
    font-size: 36px;
    font-weight: bold;
}

/* Subheaders */
.subheader {
    color: #ff9f43;
}

/* Text input styling */
div.stTextInput > div > div > input {
    color: white;
    background-color: #2a2a3c;
    border: none;
    border-radius: 5px;
    padding: 5px;
    font-size: 16px;
}

/* Placeholder color */
div.stTextInput > div > div > input::placeholder {
    color: #cccccc;
    opacity: 1;
}

/* Button styling */
div.stButton > button {
    background-color: #00d4ff;
    color: black;
    font-weight: bold;
    border-radius: 10px;
    height: 45px;
    width: 180px;
}
div.stButton > button:hover {
    background-color: #00a1cc;
    color: white;
}

/* Forecast table headers */
.forecast-table th {
    background-color: #4d4d4d;
    color: #ff9f43;
    padding: 5px;
}

/* Forecast table cells */
.forecast-table td {
    background-color: #2a2a3c;
    color: #ffffff;
    padding: 5px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# ---- TITLE ----
st.markdown('<div class="title">🌦️ Weather Forecaster</div>', unsafe_allow_html=True)

# ---- CITY INPUT WITH STYLING (LOOKS LIKE YOUR HTML) ----
st.markdown('<div style="color:white; font-weight:bold; font-size:16px; margin-bottom:5px;">Enter city name</div>', unsafe_allow_html=True)
city = st.text_input("", placeholder="e.g., Indore,IN")

# ---- GET WEATHER BUTTON ----
if st.button("Get Weather") and city.strip() != "":
    weather = get_weather(city)
    if weather:
        # CURRENT WEATHER
        st.markdown(f"<h3 class='subheader'>Current Weather in {weather['city']}</h3>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#00ff9f; font-size:20px; font-weight:bold;'>Temperature: {weather['temperature']}°C</p>", unsafe_allow_html=True)
        st.markdown(f"<p style='color:#ffcc66; font-size:18px;'>Condition: {weather['description'].title()}</p>", unsafe_allow_html=True)

        # 3-DAY FORECAST
        forecast = get_forecast(city)
        if forecast:
            st.markdown("<h3 class='subheader'>3-Day Forecast</h3>", unsafe_allow_html=True)

            # Prepare table data
            table_data = []
            for f in forecast[:24]:  # first 3 days (8 records/day)
                date, time = f['datetime'].split(' ')
                table_data.append({
                    "Date": date,
                    "Time": time,
                    "Temp (°C)": f['temp'],
                    "Condition": f['description'].title()
                })

            df = pd.DataFrame(table_data)

            # Color temperatures dynamically
            def color_temp(val):
                if val >= 30:
                    color = '#ff6666'  # warm red
                elif val >= 20:
                    color = '#ffa500'  # orange
                else:
                    color = '#00ff9f'  # mint green
                return f'color: {color}; font-weight:bold'

            st.dataframe(df.style.applymap(color_temp, subset=['Temp (°C)']), use_container_width=True)
    else:
        st.error("City not found or API error.")

# ---- SEARCH HISTORY ----
st.markdown("<h3 class='subheader'>Search History</h3>", unsafe_allow_html=True)
history = load_history()
if history:
    for item in reversed(history[-10:]):
        st.markdown(f"<p style='color:#a3a3ff'>{item['city']}: {item['temperature']}°C, {item['description'].title()}</p>", unsafe_allow_html=True)
else:
    st.write("No search history found.")
