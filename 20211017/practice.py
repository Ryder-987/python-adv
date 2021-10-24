from tkinter import *
import requests, json
import matplotlib.pyplot as plt
def get_data():    
    api_key = "2f7671995fd280c1b8c10843d66b3f93"
    base_url = "https://api.openweathermap.org/data/2.5/onecall?"
    exclude = "minutely,hourly"
    units = "metric"
    lang = "zh_tw"
    lat = lat_info.get()
    lon = lon_info.get()

    send_url = base_url
    send_url += "lat=" + lat
    send_url += "&lon=" + lon
    send_url += "&exclude=" + exclude
    send_url += "&appid=" + api_key 
    send_url += "&units=" + units 
    send_url += "&lang=" + lang

    response = requests.get(send_url)
    info = json.loads(response.text)

    days = [
    put_day1.config, put_day2.config, put_day3.config, put_day4.config,
    put_day5.config, put_day6.config, put_day7.config
]
    list_temp = []
    try:
        if info['lat']!="":
            for i in range(8):
                temps = info['daily'][i]['temp']['day']
                list_temp.append(temps)
                print('Day%d Temp=%s C' %(i,temps))
                days[i](text="Day%d Temp=%s C" % (i, temps))
            
            plt.plot(range(1,8) ,list_temp)
            plt.show
    except:
        print('Request fail')

windows = Tk()
windows.title("My Weather")

put_day1 = Label(windows, text="day1:")
put_day1.pack()

put_day2 = Label(windows, text="day2:")
put_day2.pack()

put_day3 = Label(windows, text="day3:")
put_day3.pack()

put_day4 = Label(windows, text="day4:")
put_day4.pack()

put_day5 = Label(windows, text="day5:")
put_day5.pack()

put_day6 = Label(windows, text="day6:")
put_day6.pack()

put_day7 = Label(windows, text="day7:")
put_day7.pack()

hint = Label(windows, text="請輸入經度")
hint.pack()

lat_info = Entry(windows)
lat_info.pack()

hint = Label(windows, text="請輸入緯度")
hint.pack()

lon_info = Entry(windows)
lon_info.pack()

btn = Button(windows, text='get weather', command=get_data)
btn.pack()

windows.mainloop()