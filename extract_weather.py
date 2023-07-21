import requests
import json
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()


api_key = os.environ["API_KEY"]

# Set the location that you want to get the weather data for
country = input("Country: ")
city = input("City: ")
df_country_code = pd.read_csv(
    "country_code.csv", names=["country", "code"], encoding="ISO-8859-1", sep=";"
)

country_code = df_country_code[df_country_code["country"] == country][
    "code"
].to_string()
print(country_code)
url = "https://api.openweathermap.org/data/2.5/weather?q={city},{country_code}&appid={api_key}".format(
    city=city, country_code=country_code, api_key=api_key
)

response = requests.get(url)

# Check if the response was successful
if response.status_code == 200:

    # Get the weather data from the response
    weather_data = json.loads(response.content.decode())

    temp = weather_data["main"]["temp"]
    temp_max = weather_data["main"]["temp_max"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    wind_speed = weather_data["wind"]["speed"]
    weather_description = weather_data["weather"][0]["description"]

    # Print the temperature, maximum temperature, feels like, humidity, wind speed and the weather description
    print("The temperature is:", temp - 273.15, "degrees Celsius")
    print("The maximum temperature is:", temp_max - 273.15, "degrees Celsius")
    print("The feels like temperature is:", feels_like - 273.15, "degrees Celsius")
    print("The humidity is:", humidity, "%")
    print("The wind speed is:", wind_speed, "m/s")
    print("The weather description is:", weather_description)


else:

    # Print the error message
    print(response.status_code)
    print(response.content)
