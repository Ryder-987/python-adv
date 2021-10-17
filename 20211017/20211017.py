# import matplotlib.pyplot as plt

# listX=[1,2,3,4,5,6]
# listY=[20,30,37,21,33,40]

# plt.plot(listX,listY)
# plt.show()

import requests, json
 
api_key = "2f7671995fd280c1b8c10843d66b3f93"
base_url = "https://api.openweathermap.org/data/2.5/onecall?"
exclude = "minutely,hourly"
units = "metric"
lang = "zh_tw"

lat = input('Enter latitude:')
lon = input('Enter longitude:')

send_url = base_url
send_url += "lat=" + lat
send_url += "&lon=" + lon
send_url += "&exclude=" + exclude
send_url += "&appid=" + api_key 
send_url += "&units=" + units 
send_url += "&lang=" + lang

response = requests.get(send_url)
info = json.loads(response.text)

try:
    if info['lat']!="":
        for i in range(7):
            temps = info['daily'][i]['temp']['day']
            print('Day%d Temp=%s C' %(i,temps))
except:
    print('Request fail')