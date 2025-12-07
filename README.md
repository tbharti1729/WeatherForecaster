# 🌦️ Weather Forecaster

A Python-based Weather Forecaster that fetches real-time weather data for any city using OpenWeatherMap API. Stores search history in JSON and optionally displays a 3-day forecast. Supports CLI and Streamlit interface.

## Features
- Fetch current weather by city
- Save search history for offline access
- Multi-day forecast display
- Interactive Streamlit UI
- Robust error handling

## How to Run
1. Install dependencies:

2. Replace `YOUR_API_KEY_HERE` in `weather_fetcher.py` with your OpenWeatherMap API key.
3. Run Streamlit app:

🖼️ UI Preview

The app uses a custom-designed dark theme with neon accent colors to improve readability and overall visual appeal.

📁 Project Structure
WeatherForecaster/
│── app.py                   # Streamlit UI (main app)
│── requirements.txt         # Dependencies
│── README.md                # Project documentation
│── weather/
│     ├── weather_fetcher.py # API calls + JSON storage
│     ├── weather_history.py # Search history file (JSON)
│── .env                     # Your API key (ignored by git)
│── venv/                    # Virtual environment (ignored)

🔧 Tech Stack
Component -	Tech
Frontend UI	Streamlit + Custom HTML/CSS
Backend Logic -	Python
API	 - OpenWeatherMap
Storage	 - JSON file
Styling	 - Custom CSS injected into Streamlit

🚧 Future Improvements

Add AQI (Air Quality Index)

Add historical weather graph

Auto-detect location using IP

Deploy on Streamlit Cloud

Add logging (logging module)

Write unit tests (pytest)
