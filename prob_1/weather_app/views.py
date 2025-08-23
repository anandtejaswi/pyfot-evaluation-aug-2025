# weather_app/views.py

import requests
from django.shortcuts import render
from decouple import config

def get_weather(request):
    """
    Fetches weather data from the OpenWeatherMap API based on user input,
    and renders it on the webpage.
    """
   
    api_key = config('API_KEY', default='your_api_key')
    
    
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}'

    weather_data = {}
    error_message = None

    if request.method == 'POST':
        city = request.POST.get('city_name', None)
        if city:
            try:
                city_weather = requests.get(url.format(city, api_key)).json()

                if city_weather.get('cod') == 200:
                    # Get temperature in Celsius
                    temp_celsius = city_weather['main']['temp']
                    # Convert Celsius to Kelvin
                    temp_kelvin = round(temp_celsius + 273.15, 2)

                    weather = {
                        'city': city,
                        'temperature_celsius': temp_celsius,
                        'temperature_kelvin': temp_kelvin,
                        'description': city_weather['weather'][0]['description'],
                        'icon': city_weather['weather'][0]['icon'],
                        'humidity': city_weather['main']['humidity'],
                        'wind_speed': city_weather['wind']['speed'],
                    }
                    weather_data = weather
                else:
                    error_message = f"Could not retrieve weather for '{city}'. Please check the city name or your API key."

            except requests.exceptions.RequestException:
                error_message = "Could not connect to the weather service. Please try again later."
            except KeyError:
                error_message = "An unexpected error occurred while parsing weather data."
        else:
            error_message = "Please enter a city name."


    context = {'weather_data': weather_data, 'error_message': error_message}
    return render(request, 'weather_app/weather.html', context)
