import requests
import json
input =input("city:").lower()
response = requests.get(f"https://api.openweathermap.org/geo/1.0/direct?q={input}&limit=1&appid=API-KEY")
o =response.json()
for x in o:
    b =(x["lat"])
    c=(x["lon"])




a_response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={b}&lon={c}&appid=API-KEY")
b =a_response.json()
print("Ground level",b["main"]["grnd_level"])
print("Temperature",b["main"]["pressure"])
print("TEMP MIN" ,b["main"]["temp_min"])
print("TEMP MAX",b["main"]["temp_max"])
print("Humidity",b["main"]["humidity"])
print("sea_level" ,b["main"]["sea_level"])

