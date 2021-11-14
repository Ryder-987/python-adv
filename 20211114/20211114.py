from tkinter import *
import requests
import matplotlib.pyplot as plt
import pandas as pd


def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2,
                 height,
                 str(height),
                 ha='center')


def read_YouBike():
    df = pd.read_csv("20211114/data.csv")

    Position = df.loc[:, 'Position']
    Total = df.loc[:, 'Total']
    remain = df.loc[:, 'Remain']

    btn3.config(text='顯示圖表')
    num = int(info_data.get())

    A = plt.bar(Position[:num], Total[:num], label="總車輛")
    B = plt.bar(Position[:num], remain[:num], label="剩餘車輛")

    createLabels(A)
    createLabels(B)

    plt.show()


def safe_data():
    df = pd.DataFrame(None, columns=["Position", "Total", "Remain"])


def clear_data():
    hint1.config(text="")


def get_data():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

    send_url = base_url
    response = requests.get(send_url)
    info = response.json()
    # print(send_url)
    print(safe_data)
    # print(info)
    df = pd.DataFrame(None, columns=["Position", "Total", "Remain"])
    A_list = []
    B_list = []
    C_list = []
    show = ""
    i = 0
    for num in info["retVal"]:
        if info["retVal"][num]["sarea"] == sarea_info.get():
            position_bike = (info["retVal"][num]['sna'])
            A_list.append(position_bike)
            total_bike = int(info["retVal"][num]['tot'])
            B_list.append(total_bike)
            remain_bike = int(info["retVal"][num]['sbi'])
            C_list.append(remain_bike)

            df.loc[i] = [position_bike, total_bike, remain_bike]

            hint1.config(text=show)
            i += 1

    df.to_csv("20211114/data.csv")


windows = Tk()
windows.title("My Weather")

hint = Label(windows, text="請輸入地區")
hint.pack()

sarea_info = Entry(windows)
sarea_info.pack()

hint2 = Label(windows, text='輸入獲取資料筆數')
hint2.pack()

info_data = Entry(windows)
info_data.pack()

hint1 = Label(windows, text="")
hint1.pack()

btn = Button(windows, text='獲取YouBikey資訊', command=get_data)
btn.pack()

btn2 = Button(windows, text='清除YouBikey資訊', command=clear_data)
btn2.pack()

btn3 = Button(windows, text='顯示圖表', command=read_YouBike)
btn3.pack()

windows.mainloop()