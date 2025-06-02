import date and time
import requests

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY  = open('2e8c672a07d6298cb6933578ff606cd7',r).read()
CITY = "London"

url = BASE_URL + "appid=" + API_KEY +"&q=" + CITY

response = requests.get(url).json()
print(response)
