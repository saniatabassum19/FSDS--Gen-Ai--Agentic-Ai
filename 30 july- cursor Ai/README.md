# Weather App

A modern, responsive weather application built with Python Flask and beautiful UI. Get current weather conditions and 5-day forecasts for any city around the world.

## Features

- 🌤️ **Current Weather**: Real-time temperature, humidity, wind speed, and more
- 📅 **5-Day Forecast**: Extended weather predictions with daily highs and lows
- 🎨 **Beautiful UI**: Modern, responsive design with gradient backgrounds
- 📱 **Mobile Friendly**: Works perfectly on all devices
- ⚡ **Fast & Lightweight**: Quick loading times and smooth interactions
- 🔍 **Easy Search**: Simple city search with autocomplete suggestions

## Screenshots

The app features a clean, modern interface with:
- Gradient header with search functionality
- Current weather display with detailed metrics
- 5-day forecast cards with hover effects
- Responsive design for all screen sizes

## Setup Instructions

### Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

### Installation

1. **Clone or download the project files**

2. **Install Python dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Get an API Key**:
   - Go to [OpenWeatherMap](https://openweathermap.org/api)
   - Sign up for a free account
   - Get your API key from the dashboard

4. **Configure the API Key**:
   - Open `app.py`
   - Replace `"YOUR_API_KEY_HERE"` with your actual API key
   ```python
   API_KEY = "your_actual_api_key_here"
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and go to:
   ```
   http://localhost:5000
   ```

## Usage

1. **Search for a City**: Enter any city name in the search box
2. **View Current Weather**: See temperature, humidity, wind speed, pressure, visibility, and sunrise/sunset times
3. **Check Forecast**: View 5-day weather predictions with daily highs and lows
4. **Responsive Design**: The app works perfectly on desktop, tablet, and mobile devices

## API Information

This app uses the OpenWeatherMap API which provides:
- Current weather data
- 5-day weather forecasts
- Temperature in Celsius
- Wind speed in km/h
- Pressure in hPa
- Visibility in kilometers

## File Structure

```
weather-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── README.md          # This file
└── templates/
    └── index.html     # Main HTML template with CSS and JS
```

## Customization

### Changing the API
You can easily switch to other weather APIs by modifying the `get_weather_data()` function in `app.py`.

### Styling
The CSS is embedded in the HTML template. You can modify colors, fonts, and layout by editing the `<style>` section in `templates/index.html`.

### Adding Features
- **Location Detection**: Add browser geolocation for automatic city detection
- **Weather Alerts**: Integrate severe weather warnings
- **Historical Data**: Add weather history charts
- **Multiple Units**: Add Fahrenheit/Celsius toggle

## Troubleshooting

### Common Issues

1. **"City not found" error**:
   - Check your API key is correct
   - Ensure the city name is spelled correctly
   - Try using the city name in English

2. **App won't start**:
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Check Python version: `python --version`

3. **API errors**:
   - Verify your OpenWeatherMap API key is valid
   - Check your internet connection
   - Ensure you haven't exceeded API rate limits

## Technologies Used

- **Backend**: Python Flask
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **API**: OpenWeatherMap
- **Styling**: Custom CSS with gradients and animations
- **Icons**: Font Awesome

## License

This project is open source and available under the MIT License.

## Contributing

Feel free to submit issues, feature requests, or pull requests to improve the weather app!

---

**Enjoy your weather app!** 🌤️ 