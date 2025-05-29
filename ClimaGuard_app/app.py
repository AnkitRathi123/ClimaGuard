import pandas as pd
import requests
from flask import Flask, request, render_template, redirect, flash
from datetime import datetime, timedelta
import logging
import os

log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

flask_app = Flask(__name__, template_folder='app/templates')  # Correct Flask app instance

API_KEY = '9ee744f163a54317a8f110402252705'
BASE_URL = 'https://api.weatherapi.com/v1/history.json'

def fetch_weather_data(location='singapore', days=10):
    today = datetime.today()
    results = []

    for i in range(days):
        date = (today - timedelta(days=i)).strftime('%Y-%m-%d')
        params = {
            'key': API_KEY,
            'q': location,
            'dt': date
        }
        response = requests.get(BASE_URL, params=params)
        if response.status_code == 200:
            data = response.json()
            forecast_day = data.get('forecast', {}).get('forecastday', [{}])[0]
            day_data = forecast_day.get('day', {})
            hour_data = forecast_day.get('hour', [{}])
            hour_0 = hour_data[0] if hour_data else {}

            astro_data = forecast_day.get('astro', {})

            results.append({
                'date': date,
                'max_temp': day_data.get('maxtemp_c'),
                'min_temp': day_data.get('mintemp_c'),
                'rainfall': day_data.get('totalprecip_mm'),
                'humidity': day_data.get('avghumidity'),
                'wind_kph': day_data.get('maxwind_kph'),
                'visibility_km': day_data.get('avgvis_km'),
                'uv': day_data.get('uv'),
                'sunrise': astro_data.get('sunrise'),
                'sunset': astro_data.get('sunset'),
                'moonrise': astro_data.get('moonrise'),
                'moonset': astro_data.get('moonset'),
                'moon_phase': astro_data.get('moon_phase'),

                'wind_dir': hour_0.get('wind_dir'),
                'pressure_mb': hour_0.get('pressure_mb'),
                'cloud': hour_0.get('cloud'),
                'feelslike_c': hour_0.get('feelslike_c'),
                'windchill_c': hour_0.get('windchill_c'),
                'heatindex_c': hour_0.get('heatindex_c'),
                'dewpoint_c': hour_0.get('dewpoint_c'),
                'chance_of_rain': hour_0.get('chance_of_rain'),
                'vis_km': hour_0.get('vis_km'),
                'gust_kph': hour_0.get('gust_kph')
            })
        else:
            print(f"Failed to fetch data for {date}: {response.status_code} - {response.text}")
    
    return results[::-1]



@flask_app.route('/', methods=['GET'])
def show_weather():
    weather_data = fetch_weather_data()
    today_data = weather_data[-1]
    yesterday_data = weather_data[-2]
    return render_template('index.html',
                           weather_data=weather_data,
                           today=today_data,
                           yesterday=yesterday_data)

@flask_app.route('/predict', methods=['POST'])
def predict():
    input_data = request.json
    Sample: {'max_temp': 35, 'humidity': 85}
    #Load your model here and return prediction
    result = {"heat_risk": "High", "message": "Stay hydrated and indoors"}
    return jsonify(result)

@flask_app.route('/alert', methods=['GET'])
def alert_settings():
    return render_template('alert.html')

@flask_app.route('/emergency', methods=['GET'])
def emergency_contacts():
    return render_template('emergency.html')
    
if __name__ == '__main__':
    flask_app.run(debug=True)
