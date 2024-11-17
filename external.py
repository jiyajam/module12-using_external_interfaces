##################1
import json
import requests


joke_url = "https://api.chucknorris.io/jokes/random"
try:
    response = requests.get(joke_url)
    if response.status_code == 200:
        joke = response.json()

        print("Joke: ")
        print(joke["value"])
    else:
        print("Failed to retrieve joke. Please try again later.")
except requests.exceptions.RequestException as e:
    print("Request could not be completed.")

#################2
import requests

city = input("Enter the name of a municipality: ")


api_key = "0838a1bea3d10fbbd1391556aa1ffb35"

weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

try:

    response = requests.get(weather_url)


    if response.status_code == 200:

        weather_data = response.json()


        weather_condition = weather_data["weather"][0]["description"]
        temperature_kelvin = weather_data["main"]["temp"]

        temperature_celsius = temperature_kelvin - 273.15


        print(f"Weather in {city}: {weather_condition.capitalize()}")
        print(f"Temperature: {temperature_celsius:.2f}°C")

    else:

        print(f"Failed to retrieve weather data for {city}. Please check the city name and try again.")

except requests.exceptions.RequestException as e:

    print("Request could not be completed. Please try again later.")

