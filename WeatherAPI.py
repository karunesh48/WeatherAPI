import requests

def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Weather in {city_name}:")
        print(f"Temperature: {data['main']['temp']} °C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
    else:
        print("Error fetching data:", response.status_code, response.text)

# Replace with your actual API key
API_KEY = "2e8c672a07d6298cb6933578ff606cd7"
city = input("Enter a city name: ")
get_weather(city, API_KEY)
