# python3
# Today widget
""" I wanted a script to run, every morning that I check my computer
to tell me certain aspects about my day."""

import requests, json, datetime, pytemperature
from pprint import pprint






today = datetime.date.today()

# Weather

response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip=11365,us&APPID=4be7cac5c54e583ca35b975447dd5316")
# print(response.status_code)

data = response.json()

# an example of print(data) ...

"""
{'coord': {'lon': -73.73, 'lat': 40.72}, 'weather': [{'id': 500, 'main': 'Rain',
'description': 'light rain', 'icon': '10n'}], 'base': 'stations',
'main': {'temp': 286.81, 'pressure': 1014, 'humidity': 72, 'temp_min': 284.15,
'temp_max': 289.15}, 'visibility': 16093, 'wind': {'speed': 0.28, 'deg': 188.503},
'clouds': {'all': 90}, 'dt': 1525660500, 'sys': {'type': 1, 'id': 1969, 'message': 0.0051,
'country': 'US', 'sunrise': 1525686366, 'sunset': 1525737447}, 'id': 420026213,
'name': 'New York', 'cod': 200}
"""

weather = data["main"]
clouds = data["clouds"]
json_string = json.dumps(weather)
weather = json.loads(json_string)

temp = weather["temp"]
maxtemp = weather["temp_max"]
mintemp = weather["temp_min"]

data["weather"]
wm = data["weather"]
wm = wm[0]
description = wm["description"]
# description is the type of weather; i.e. cloudy, light rain, thunderstorms, etc.

print("\n")
print(today.strftime("Today ------------ %b, %d %Y ---"))
# prints the date in m/d/Y format
print("\n")
print("Current weather is: ")
print("\n")
print(description + " and " + str(pytemperature.k2f(temp)) + " degrees")
print("------------------------------------")
print("Todays high: " + str(pytemperature.k2f(maxtemp)) + " degrees")
print("------------------------------------")
print("Todays low: " + str(pytemperature.k2f(mintemp)) + " degrees")
print("\n")
print("------------------------------------")


# quit-smoking-time
import datetime

last_day = datetime.datetime(2018, 3, 10)

how_many_days = datetime.datetime.now() - last_day
strng = str(how_many_days)
hmd = strng[0:8]
print("\n")
print("Congratulations!")
print("It's been {} since you've stopped smoking".format(hmd))

if hmd == "90":
	print("Your heart attack risk has begun to drop, and your lung function has started to improve")

money_saved = 9

total_money_saved = how_many_days * money_saved
string = str(total_money_saved)
tms = string[0:4]
print("\n")
print("You've saved ${}!".format(tms))
print("Enough for: ")

x = ("Apple AirPods = $149",
	"Gas for 1 Month = $100",
	"5 Months of Oil Changes = $152")
y = ("Apple AirPods = $149",
	"Gas for 1 Month = $100",
	"5 Months of Oil Changes = $152",
	"Adidas Ultraboost Sts = $200")
z = ("Apple AirPods = $149",
	"Gas for 1 Month = $100",
	"5 Months of Oil Changes = $152",
	"Adidas Ultraboost Sts = $200",
	"Off-Peak Round Trip Flight to SFO = $325")


if tms >= '400':
	pprint(x, width=35)
elif tms >= '600':
	pprint(y, width=35)
elif tms >= '925':
	pprint(z, width=35)
print("-----------------------------------------------")
print("How are you going to change the world today?")
print("\n")


# Stocks
""" Maybe no stocks..."""

# Titles for Breaking News articles

# What's on my schedule

# what bills are upcoming

# How do we put a GUI to this? so it's not just a CLI program
