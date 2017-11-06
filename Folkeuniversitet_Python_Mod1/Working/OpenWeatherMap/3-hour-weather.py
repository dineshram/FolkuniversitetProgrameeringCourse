#Documentation is at https://pyowm.readthedocs.org/en/latest/pyowm.html
#github documentation is at https://github.com/csparpa/pyowm/wiki/Usage-examples
#https://tasteandseejesus.com/2016/01/13/3-hour-forecasts-with-openweathermap-and-python/

#retrieve weather data
import pyowm
import json

owm = pyowm.OWM('327407589df060c7f825b63ec1d9a096')
location = "Bergen, Norway"

forecaster = owm.three_hours_forecast(location)
forecast = forecaster.get_forecast()
weather_list = forecast.get_weathers()

# establish time constant
in3hours = pyowm.timeutils.next_three_hours()

# Retreive daily forecast
forecast = owm.daily_forecast(location)

# Retrieve forecast at location in 3 hours
latertoday = forecast.get_weather_at(in3hours)
decoded_later = json.loads(latertoday.to_JSON())  # its easier to load it into JSON and decode it!
detailed_status_later = decoded_later['detailed_status']  # detailed status in 3 hours

# Search for current weather
observation = owm.weather_at_place(location)
# observation = owm.weather_at_coords(-33.73, 150.998)
w = observation.get_weather()
decoded_w = json.loads(w.to_JSON())
detailed_status = decoded_w['detailed_status']

# Create String to Print
strMsg = location + detailed_status.title() + ' (later expect ' + detailed_status_later.title() + ') from ' + str(
    w.get_temperature('celsius')['temp_min']) + 'C to ' + str(w.get_temperature('celsius')['temp_max']) + 'C, ' + str(
    decoded_w['humidity']) + '% humidity &amp;amp;amp; ' + str(decoded_w['clouds']) + '% cloud'
print(strMsg)