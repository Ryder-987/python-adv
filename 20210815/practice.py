from tkinter import *

def show_fun():
    print("Hello Singular")
    display.config(text="Hi Singular", fg="black", bg="#FF9F00")

def clear_fun():
    print("Hello Singular")
    display.config(text="Hi Singular", fg="white", bg="white")

windows = Tk()
windows.title("My first GUI")

btn1 = Button(windows, text="show screen", command=show_fun)
btn1.pack()

btn2 = Button(windows, text="clear screen", command=clear_fun)
btn2.pack()

windows.mainloop()