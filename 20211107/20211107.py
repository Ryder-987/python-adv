from tkinter import *
import requests
import matplotlib.pyplot as plt


def clear_data():
    hint1.config(text="")


def get_data():
    base_url = "https://tcgbusfs.blob.core.windows.net/blobyoubike/YouBikeTP.json"

    send_url = base_url
    response = requests.get(send_url)
    info = response.json()
    # print(send_url)

    # print(info)
    A_list = []
    B_list = []
    C_list = []
    show = ""
    for num in info["retVal"]:
        if info["retVal"][num]["sarea"] == sarea_info.get():
            print("地點:" + info["retVal"][num]['sna'])
            A_list.append(info["retVal"][num]["sna"])
            print("總共車輛:" + info["retVal"][num]['tot'])
            B_list.append(int(info["retVal"][num]['tot']))
            print("剩餘車輛:" + info["retVal"][num]['sbi'])
            C_list.append(int(info["retVal"][num]['sbi']))
            print("地區:" + info["retVal"][num]["sarea"])
            print()
            show += "地點:" + info["retVal"][num]['sna'] + "總共車輛:" + info[
                "retVal"][num]['tot'] + "剩餘車輛:" + info["retVal"][num][
                    'sbi'] + "地區:" + info["retVal"][num]["sarea"] + '\n'
            hint1.config(text=show)

    plt.plot(A_list, B_list, "c-o", label="總車輛")
    plt.plot(A_list, C_list, "b--", label="剩餘車輛")
    plt.legend(loc="upper left")
    plt.show()


windows = Tk()
windows.title("My Weather")

hint = Label(windows, text="請輸入地區")
hint.pack()

sarea_info = Entry(windows)
sarea_info.pack()

hint1 = Label(windows, text="")
hint1.pack()

btn = Button(windows, text='綁架YouBikey資訊', command=get_data)
btn.pack()

btn2 = Button(windows, text='消滅YouBikey資訊', command=clear_data)
btn2.pack()

windows.mainloop()