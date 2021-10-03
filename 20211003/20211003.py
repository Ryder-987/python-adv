import requests
import json
book = {'書名': '海邊的卡夫卡', '作者': '春上春樹'}
print(book['書名'])
print(book['作者'])

book['書名'] = '七龍珠'
book['作者'] = '烏山明'
print(book['書名'])
print(book['作者'])

keys = book.keys()
for key in book.keys():
    print(key)

values = book.values()
for value in book.values():
    print(value)

data = {"Name": "Singular","Score": [{"Math": 100, "English": 99}, {"Chinese": 98, "Nature": 97}]}

api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "http://api.openweathermap.org/data/2.5/weather?"
city_name = input("Enter city name : ")
units = "metric"
lang = "zh_tw"

send_url = base_url
send_url += "appid=" + api_key
send_url += "&q=" + city_name
send_url += "&units=" + units
send_url += "&lang=" + lang

print("%s\n" % send_url)
response = requests.get(send_url)
info = response.json()
print(info)


info = {
    "coord": {
        "lon": 121.5319,
        "lat": 25.0478
    },
    "weather": [{
        "id": 801,
        "main": "Clouds",
        "description": "晴，少雲",
        "icon": "02d"
    }],
    "base":
    "stations",
    "main": {
        "temp": 28.64,
        "feels_like": 32.64,
        "temp_min": 26.98,
        "temp_max": 30.07,
        "pressure": 1014,
        "humidity": 74
    },
    "visibility":
    10000,
    "wind": {
        "speed": 3.58,
        "deg": 90,
        "gust": 8.05
    },
    "clouds": {
        "all": 20
    },
    "dt":
    1632616331,
    "sys": {
        "type": 2,
        "id": 266033,
        "country": "TW",
        "sunrise": 1632606230,
        "sunset": 1632649603
    },
    "timezone":
    28800,
    "id":
    1668341,
    "name":
    "Taipei",
    "cod":
    200
}

print(info['weather'][0]['description'])
print(info['main']['temp'])