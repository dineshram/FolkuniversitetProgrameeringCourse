__author__ = 'dram'

#https://home.openweathermap.org/
#superman / standard Pappu
#API KEY = dbf6aaf008f3591e4eeb64257fd2d985, students = 279109b954115b5c2a32711113ca2fcd pro: 327407589df060c7f825b63ec1d9a096
#http://bigl.es/using-python-to-get-weather-data/

# from pprint import pprint
# import requests
#
# city = input("Please Enter City >  ")
# url = "http://api.openweathermap.org/data/2.5/weather?q=" + city
# print(url)
# r = requests.get(url)
# pprint(r.json())

import pyowm

owm = pyowm.OWM('dbf6aaf008f3591e4eeb64257fd2d985')
location = "Bergen, Norway"
observation = owm.weather_at_place(location)
weather = observation.get_weather()

wind = weather.get_wind()
temperature = weather.get_temperature('celsius')
tomorrow = pyowm.timeutils.tomorrow()

print(weather)
print("The wind at :", location, " is", wind)
print("The temperaure at :", location, " is", temperature)
print(tomorrow)
