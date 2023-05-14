import json
import os

import requests

print("Welcome to the \'Weather App\'")

city = input("Enter the name of the city: ")

url = f"http://api.weatherapi.com/v1/current.json?key=YOUR_API_KEY&q={city}"

r = requests.get(url)
dict = json.loads(r.text)
w = dict["current"]["temp_c"]
f = dict["current"]["temp_f"]

command = f"say 'The weathr of the city{city}in degree celsius is{w} and degree fahrenheit is{f}'"
os.system(command)

print("Weather in degree celsius =", w, "\nWeather in degree fahrenheit", f)
