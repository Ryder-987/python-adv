from tkinter import *
import datetime

def get_date():
    time = datetime.date.today()
    display.config(text=str(time), fg="black")

def get_time():
    time = datetime.datetime.now().time()
    display.config(text=str(time), fg="red")

def display_entry():
    display.config(text=input_data.get(), fg="black")

windows = Tk()
windows.title("My first GUI")

btn1 = Button(windows, text="獲得今天日期", command=get_date)
btn1.pack()

btn2 = Button(windows, text="獲得今天時間", command=get_time)
btn2.pack()

display = Label(windows, text="")
display.pack()

input_data = Entry(windows)
input_data.pack()

btn3 = Button(windows, text="顯示輸入的文字", command=display_entry)
btn3.pack()


windows.mainloop()