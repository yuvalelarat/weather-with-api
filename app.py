from urllib import response
import requests

API_KEY = "58ab05985529bd48b069fa9ac9d02754"
BASE_URL ="https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    temperature = round(data["main"]["temp"] - 272.15)

    print("The weather is", weather, "and the temperature:",temperature, "celsuis")
else:
    print("An error occurred")


