# -*- coding: utf-8 -*-
"""Weather.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14rwuH15EQp9uVeekJyAHHVfhB_PaLmc-
"""

import requests
from datetime import datetime

api_key = '08af8db991ccccc122fa962362abf9de'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main'] ['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
coor_d= api_data['coord']
hmdt = api_data['main']['humidity']
visib = api_data['visibility']
wind_spd = api_data['wind']['speed']
time_zone= api_data['timezone']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------")
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time))
print ("-------------------------------------------------------------")

print ("Current temperature is: {:.2f} deg C".format(temp_city))
print ("Current weather desc  :",weather_desc)
print ("Current Coordination  :",coor_d)
print ("Current Humidity      :",hmdt, '%')
print ("Current Visibility    :",visib)
print ("Current wind speed    :",wind_spd ,'kmph')
print ("current Timezone      :",time_zone)