import json
import requests
import pprint

api = '6927d88cf63a83785732f1bc32728ef0'

print("Enter a City Name: ")
city = raw_input()
city = str(city)

with open('city.list.json', 'r') as f:
     idData = json.load(f)

i = 0
while True:
	cityName = idData[i]['name']
	if cityName == city:
		cityId = idData[i]['id']
		break
	i = i+1

print('http://api.openweathermap.org/data/2.5/forecast?id='+str(cityId)+'&APPID='+api)
r = requests.get('http://api.openweathermap.org/data/2.5/forecast?id='+str(cityId)+'&APPID='+api)

weatherData = r.json()

print json.dumps(weatherData, indent=4, sort_keys=True)


city = weatherData["city"]
country = city["country"]
ID = city["id"]
name = city["name"]
coord = city["coord"]
lon = coord["lon"]
lat = coord["lat"]

cnt = weatherData["cnt"]
cod = weatherData["cod"]

weatherList = weatherData["list"]
i = 0
while i < cnt
	current = weatherList[i]
	clouds = current["clouds"]
	dt_txt = current["dt_txt"]
	main = current["main"]





#weather = weatherData["weather"]
#main = weatherData["main"]
#wind = weatherData["wind"]
#rain = weatherData["rain"]
#clouds = weatherData["clouds"]
#dt = weatherData["dt"]
#sys = weatherData["sys"]


	