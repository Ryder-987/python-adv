from tkinter import *
import requests
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def createLabels(data):
    for item in data:
        height = item.get_height()
        plt.text(item.get_x() + item.get_width() / 2,
                 height,
                 str(height),
                 ha='center')


df = pd.DataFrame(None, columns=["日期", "主場勝", "客場勝"])

base_url = 'https://tw.global.nba.com/stats2/scores/daily.json?'
contry = 'TW'
date = '2021-11-1'
locale = 'zh_TW'
tz = '%2B8'

send_url = base_url
send_url += '?countryCode=' + contry
send_url += '&gameDate' + date
send_url += '&locale' + locale
send_url += '&tz' + tz

response = requests.get(send_url)
info = response.json()

print(send_url)

game_date = []
cust_win_list = []
home_win_list = []

data = info['payload']['date']['games']

home_win = 0
cust_win = 0

for num in data:
    print("cust : {}".format(num['boxscore']['awayScore']))
    print('home : {}'.format(num['boxscore']['homeScore']))
    if num['boxscore']['awayScore'] > num['boxscore']['homeScore']:
        cust_win += 1
    else:
        home_win += 1

print(home_win)
print(cust_win)

df = df.append({
    '日期': date,
    '主場勝': home_win,
    '客場勝': cust_win
},
               ignore_index=True)

game_date.append(date)
cust_win_list.append(cust_win)
home_win_list.append(home_win)

index = np.arange(len(game_date))
fig, ax = plt.subplots()

A = ax.bar(index, cust_win_list, label="客場勝", width=0.25)
B = ax.bar(index + 0.25, home_win_list, label="主場勝", width=0.25)

ax.set_xticks(index)
ax.set_xticklabels(game_date)
createLabels(A)
createLabels(B)

plt.legend(loc=1)
plt.show()

df.to_csv('20211118/data.csv')