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
        clip = clip.subclip(int(start_time), int(end_time))
        i = 0
        base_path = '20211205/'
        new_file = get_name
        new_path = base_path + new_file + str(i) + '.mp4'

        while os.path.isfile(new_path):
            i += 1
            new_path = base_path + new_file + str(i) + '.mp4'

        clip.write_videofile(new_path)
        if (state.get()):
            print('checkval = True')
            clip.write_gif(base_path + new_file + str(i) + '.gif')
    else:
        exit()


windows = Tk()
windows.title("My Weather")

hint = Label(windows, text="請輸入影片名字")
hint.grid(row=0, column=0)

name_info = Entry(windows)
name_info.grid(row=0, column=1)

hint1 = Label(windows, text="開始時間")
hint1.grid(row=1, column=0)

strat_info = Entry(windows)
strat_info.grid(row=1, column=1)

hint2 = Label(windows, text='結束時間')
hint2.grid(row=2, column=0)

end_info = Entry(windows)
end_info.grid(row=2, column=1)

state = BooleanVar()
state.set(True)
chk = Checkbutton(windows, text='gif', var=state)
chk.grid(row=3, column=0)

btn1 = Button(windows, text='開始切割', command=cut_video)
btn1.grid(row=3, columnspan=2)

windows.mainloop()