from turtle import title
from urllib import request
import requests
import json
from plyer import notification
import timeouts
import time

# You have to get thi api key from the website
API_KEY="c00dd41b11437c7fe4fad443bd1770e8"
Base_URL="https://api.openweathermap.org/data/2.5/weather"

city=input("Please enter the city name : ")
request_url=f"{Base_URL}?q={city}&appid={API_KEY}"

responce=requests.get(request_url)
print(responce)

if responce.status_code==200 :
    data=responce.json()
   
    weather=data["weather"]
    print(weather)
    main=round(data["main"]['temp']-273.15)
    print(main)

# Sending the notification to desktop   
a=f"Current temperature at {city} is {main} degree celc"
while(True):
    time.sleep(5)
    notification.notify(
        title="Current weather",
        message=a,
        timeout=0,

)

