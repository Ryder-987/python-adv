from tkinter import *
from pytube import YouTube
from moviepy.editor import VideoFileClip


def get_video():
    get_url = url_info.get()
    get_name = name_info.get() + 'mp4'

    yt = YouTube(get_url)
    video = yt.streams
    length = len(video)

    for i in range(length):
        print(video[i])

    print('影片名稱', yt.title)
    print('影片作者', yt.author)
    print('影片長度', yt.length, '秒')
    print('縮圖網址', yt.thumbnail_url)

    result = video.filter(progressive=True, subtype='mp4', res='360p')
    print(result[0])

    dest = '20211203'
    fname = get_name

    result[0].download(output_path=dest, filename=fname)
    print('Download finished ...')

    movie_name.config(text='電影名稱 =' + get_name)
    movie_time.config(text='電影時間 =' + str(yt.length) + 'sec')

    clip = VideoFileClip(dest + fname)
    clip.preview()


windows = Tk()
windows.title("My Weather")

hint = Label(windows, text="請輸入影片網址")
Label.grid(row=0, column=0)

hint1 = Label(windows, text="請輸入影片名稱")
Label.grid(row=1, column=0)

btn1 = Button(windows, text='Download', command=get_video)
Button.grid(row=2, column=1, columnspan=2)
