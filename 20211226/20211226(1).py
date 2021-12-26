from tkinter import *


def show_info():
    chk = state.get()

    if (chk):
        box_label.grid(sticky='w')
    else:
        box_label.grid_forget()


windows = Tk()
windows.title('My grid')

box_label = Label(windows, text='lable info')

state = BooleanVar()
state.set(False)
box = Checkbutton(windows, text='show info', var=state, command=show_info)
box.grid(sticky='w')

windows.geometry('300x150')
windows.mainloop()