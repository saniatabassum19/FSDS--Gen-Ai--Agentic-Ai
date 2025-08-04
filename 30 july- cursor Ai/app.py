from flask import Flask, render_template, request, jsonify
import requests
import os
from datetime import datetime, timedelta

app = Flask(__name__)

# OpenWeatherMap API configuration
API_KEY = "YOUR_API_KEY_HERE"  # Replace with your actual API key
BASE_URL = "http://api.openweathermap.org/data/2.5"

def get_weather_data(city):
    """Fetch current weather data for a city"""
    try:
        # Current weather
        current_url = f"{BASE_URL}/weather"
        params = {
            'q': city,
            'appid': API_KEY,
            'units': 'metric'
        }
        
        response = requests.get(current_url, params=params)
        response.raise_for_status()
        current_data = response.json()
        
        # 5-day forecast
        forecast_url = f"{BASE_URL}/forecast"
        response = requests.get(forecast_url, params=params)
        response.raise_for_status()
        forecast_data = response.json()
        
        return {
            'current': current_data,
            'forecast': forecast_data
        }
    except requests.RequestException as e:
        return None

def format_weather_data(weather_data):
    """Format weather data for display"""
    if not weather_data:
        return None
    
    current = weather_data['current']
    forecast = weather_data['forecast']
    
    # Format current weather
    current_weather = {
        'city': current['name'],
        'country': current['sys']['country'],
        'temperature': round(current['main']['temp']),
        'feels_like': round(current['main']['feels_like']),
        'description': current['weather'][0]['description'].title(),
        'icon': current['weather'][0]['icon'],
        'humidity': current['main']['humidity'],
        'wind_speed': round(current['wind']['speed'] * 3.6, 1),  # Convert m/s to km/h
        'pressure': current['main']['pressure'],
        'visibility': round(current['visibility'] / 1000, 1),  # Convert to km
        'sunrise': datetime.fromtimestamp(current['sys']['sunrise']).strftime('%H:%M'),
        'sunset': datetime.fromtimestamp(current['sys']['sunset']).strftime('%H:%M')
    }
    
    # Format forecast data (daily forecasts)
    daily_forecasts = []
    seen_dates = set()
    
    for item in forecast['list']:
        date = datetime.fromtimestamp(item['dt']).date()
        if date not in seen_dates and len(daily_forecasts) < 5:
            seen_dates.add(date)
            daily_forecasts.append({
                'date': datetime.fromtimestamp(item['dt']).strftime('%A'),
                'day': datetime.fromtimestamp(item['dt']).strftime('%d'),
                'month': datetime.fromtimestamp(item['dt']).strftime('%b'),
                'temp_max': round(item['main']['temp_max']),
                'temp_min': round(item['main']['temp_min']),
                'description': item['weather'][0]['description'].title(),
                'icon': item['weather'][0]['icon'],
                'humidity': item['main']['humidity']
            })
    
    return {
        'current': current_weather,
        'forecast': daily_forecasts
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    weather_data = get_weather_data(city)
    if weather_data:
        formatted_data = format_weather_data(weather_data)
        if formatted_data:
            return jsonify({'success': True, 'data': formatted_data})
    
    return jsonify({'success': False, 'error': 'City not found or API error'})

@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get('city', '').strip()
    if not city:
        return jsonify({'success': False, 'error': 'Please enter a city name'})
    
    weather_data = get_weather_data(city)
    if weather_data:
        formatted_data = format_weather_data(weather_data)
        if formatted_data:
            return jsonify({'success': True, 'data': formatted_data})
    
    return jsonify({'success': False, 'error': 'City not found. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000) 