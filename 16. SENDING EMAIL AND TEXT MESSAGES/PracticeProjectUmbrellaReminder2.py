import requests
from twilio.rest import Client
import schedule
import time

# Twilio Account SID, Auth Token, and Twilio phone number
account_sid = 'your_twilio_account_sid'
auth_token = 'your_twilio_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'your_phone_number'

# OpenWeatherMap API key
owm_api_key = 'your_openweathermap_api_key'

# Function to check weather and send SMS
def check_weather_and_send_sms():
    # Specify the city name for the desired location (e.g., Dhaka)
    city_name = 'Dhaka'
    country_code = 'BD'  # Country code for Bangladesh

    # Build the OpenWeatherMap URL
    weather_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name},{country_code}&appid={owm_api_key}'

    # Send a GET request to the URL
    response = requests.get(weather_url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the weather condition from the JSON response
        weather_data = response.json()
        weather_condition = weather_data['weather'][0]['description']

        # Send SMS using Twilio
        client = Client(account_sid, auth_token)
        if 'rain' in weather_condition.lower():
            message_body = f'It\'s raining in {city_name}. Remember to pack an umbrella!'
        else:
            message_body = f'It\'s not raining in {city_name}. No need for an umbrella.'

        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        print(f"SMS sent: {message.sid}")
    else:
        print(f"Failed to retrieve weather information. Status code: {response.status_code}")

# Schedule the job to run every day at 08:00 AM
schedule.every().day.at("08:00").do(check_weather_and_send_sms)

# Run the scheduled jobs
while True:
    schedule.run_pending()
    time.sleep(1)
