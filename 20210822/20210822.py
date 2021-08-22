from tkinter import *

def move_canvas(event):
    key = event.keysym
    print(key)
    if key == "d":
        canvas.move(circle, 10, 0)
    elif key == "a":
        canvas.move(circle, -10, 0)
    elif key =="w":
        canvas.move(circle, 0, -10)
    elif key =="s":
        canvas.move(circle, 0, 10)

windows = Tk()
windows.title("My first GUI")

canvas = Canvas(windows, width=400, height=600)
canvas.pack()

windows.iconbitmap("20210822/888-1604030125.ico")
img = PhotoImage(file="20210822/crocodile2.gif")
my_img = canvas.create_image(200, 400, image=img)

circle = canvas.create_oval(100, 100, 300, 300, fill="#6AFFCA")
rect = canvas.create_rectangle(220, 400, 340, 430, fill="black")
msg = canvas.create_text(200, 80, text="Corcodile", fill="black", font=('ALGERIAN', 30))

canvas.bind_all('<Key>', move_canvas)

windows.mainloop()