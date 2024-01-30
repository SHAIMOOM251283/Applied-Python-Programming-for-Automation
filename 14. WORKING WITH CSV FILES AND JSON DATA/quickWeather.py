import sys
import requests
import json

def get_weather(location):
    api_key = 'API_KEY_FROM_OPENWEATHER'  # Replace with your API key from OpenWeatherMap

    # OpenWeatherMap API endpoint for current weather
    endpoint = 'http://api.openweathermap.org/data/2.5/weather'
    
    # Parameters for the API request
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # You can change to 'imperial' for Fahrenheit
    }

    # Make the API request
    response = requests.get(endpoint, params=params)

    if response.status_code == 200:
        # Parse the JSON data
        weather_data = json.loads(response.text)

        # Print the current weather
        print(f"Weather in {location} today:")
        print(f"Description: {weather_data['weather'][0]['description']}")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Humidity: {weather_data['main']['humidity']}%")
        print()

        # OpenWeatherMap API endpoint for 3-day forecast
        forecast_endpoint = 'http://api.openweathermap.org/data/2.5/forecast'
        params['cnt'] = 8  # Request 8 data points for the next 3 days

        # Make the forecast API request
        forecast_response = requests.get(forecast_endpoint, params=params)

        if forecast_response.status_code == 200:
            # Parse the JSON forecast data
            forecast_data = json.loads(forecast_response.text)

            # Print the forecast for the next two days
            print("Weather forecast for the next two days:")
            for i in range(1, 3):
                date = forecast_data['list'][i]['dt_txt']
                description = forecast_data['list'][i]['weather'][0]['description']
                temperature = forecast_data['list'][i]['main']['temp']
                print(f"{date}: {description}, Temperature: {temperature}°C")

        else:
            print(f"Failed to fetch forecast data. Status code: {forecast_response.status_code}")

    else:
        print(f"Failed to fetch weather data. Status code: {response.status_code}")

if __name__ == "__main__":
    # Get location from command line arguments
    location = ' '.join(sys.argv[1:])

    if not location:
        print("Please provide a location as a command line argument.")
    else:
        get_weather(location)
