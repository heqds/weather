import requests

API_KEY = "API_KEY_HERE"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
print ("------------------------")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15)
    feels_like = round(data["main"]["feels_like"] - 273.15)
    temp_min = round(data["main"]["temp_min"] - 273.15)
    temp_max = round(data["main"]["temp_max"] - 273.15)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
    print("Feels like:", feels_like)
    print("Temperature minimum:", temp_min)
    print("Temperature max", temp_max)

    input()
    
else:
    print("Error please enter a valid city.")
