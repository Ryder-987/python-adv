from tkinter import *
import datetime

def get_number():
    ans = str(float(input_data.get())*2.54)
    display.config(text=ans, fg="black")

windows = Tk()
windows.title("My first GUI")

hint = Label(windows, text="請輸入英吋")
hint.pack()

display = Label(windows, text="")
display.pack()

input_data = Entry(windows)
input_data.pack()

btn1 = Button(windows, text="轉換公分", command=get_number)
btn1.pack()

windows.mainloop()