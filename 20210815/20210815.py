from tkinter import *

def hi_fun():
    print("Hello Singular")
    display.config(text="Hi Singular", fg="black", bg="#FF9F00")

windows = Tk()
windows.title("My first GUI")

btn = Button(windows, text="Click Me", command=hi_fun)
btn.pack()

display = Label(windows, text="hi", fg = "#5DF8FF", bg = "black")
display.pack()

windows.mainloop()