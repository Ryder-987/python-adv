import os
from pytube import YouTube
from moviepy.editor import *
from tkinter import *


def cut_video():
    get_name = name_info.get()
    start_time = strat_info.get()
    end_time = end_info.get()

    video_path = '20211203/video.mp4'
    if os.path.isfile(video_path):

        clip = VideoFileClip(video_path)
        if (state.get()):
            clip = clip.subclip(int(start_time), int(end_time))
        i = 0
        base_path = '20211226/'
        new_file = get_name
        new_path = base_path + new_file + str(i) + '.mp3'

        while os.path.isfile(new_path):
            i += 1
            new_path = base_path + new_file + str(i) + '.mp3'

        clip.audio.write_audiofile(new_path)
    else:
        exit()


def show_info():
    chk = state.get()

    if (chk):
        hint1.grid(row=1, column=0)
        strat_info.grid(row=1, column=1)
        hint2.grid(row=2, column=0)
        end_info.grid(row=2, column=1)
    else:
        hint1.grid_forget()
        strat_info.grid_forget()
        hint2.grid_forget()
        end_info.grid_forget()


windows = Tk()
windows.title("My Weather")

hint = Label(windows, text="請輸入影片名字")
hint.grid(row=0, column=0)

name_info = Entry(windows)
name_info.grid(row=0, column=1)

hint1 = Label(windows, text="開始時間")

strat_info = Entry(windows)

hint2 = Label(windows, text='結束時間')

end_info = Entry(windows)

state = BooleanVar()
state.set(False)
box = Checkbutton(windows, text='mp3', var=state, command=show_info)
box.grid(row=3)

btn1 = Button(windows, text='開始切割', command=cut_video)
btn1.grid(row=3, columnspan=2)

windows.mainloop()