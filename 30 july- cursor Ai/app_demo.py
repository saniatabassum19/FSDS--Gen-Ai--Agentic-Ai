from flask import Flask, render_template, request, jsonify
import random
from datetime import datetime, timedelta

app = Flask(__name__)

def get_mock_weather_data(city):
    """Generate mock weather data for demonstration"""
    # Mock weather conditions
    conditions = [
        "Clear sky", "Few clouds", "Scattered clouds", "Broken clouds",
        "Shower rain", "Rain", "Thunderstorm", "Snow", "Mist"
    ]
    
    # Generate current weather
    current_temp = random.randint(15, 35)
    feels_like = current_temp + random.randint(-3, 3)
    humidity = random.randint(40, 90)
    wind_speed = random.randint(5, 25)
    pressure = random.randint(1000, 1020)
    visibility = random.randint(5, 15)
    
    current_weather = {
        'city': city.title(),
        'country': 'Demo',
        'temperature': current_temp,
        'feels_like': feels_like,
        'description': random.choice(conditions),
        'icon': '01d',  # Default sunny icon
        'humidity': humidity,
        'wind_speed': wind_speed,
        'pressure': pressure,
        'visibility': visibility,
        'sunrise': '06:30',
        'sunset': '18:45'
    }
    
    # Generate 5-day forecast
    forecast = []
    for i in range(1, 6):
        date = datetime.now() + timedelta(days=i)
        temp_max = random.randint(20, 35)
        temp_min = random.randint(10, 25)
        
        forecast.append({
            'date': date.strftime('%A'),
            'day': date.strftime('%d'),
            'month': date.strftime('%b'),
            'temp_max': temp_max,
            'temp_min': temp_min,
            'description': random.choice(conditions),
            'icon': '01d',
            'humidity': random.randint(40, 90)
        })
    
    return {
        'current': current_weather,
        'forecast': forecast
    }

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/weather/<city>')
def get_weather(city):
    weather_data = get_mock_weather_data(city)
    return jsonify({'success': True, 'data': weather_data})

@app.route('/search', methods=['POST'])
def search_weather():
    city = request.form.get('city', '').strip()
    if not city:
        return jsonify({'success': False, 'error': 'Please enter a city name'})
    
    weather_data = get_mock_weather_data(city)
    return jsonify({'success': True, 'data': weather_data})

if __name__ == '__main__':
    print("🌤️  Weather App Demo Starting...")
    print("📱 Open your browser and go to: http://localhost:5000")
    print("🔑 This is a demo version with mock data - no API key required!")
    print("💡 To use real weather data, run 'python app.py' instead")
    app.run(debug=True, host='0.0.0.0', port=5000) 