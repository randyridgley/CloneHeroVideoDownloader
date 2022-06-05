import configparser
import glob
import os
import time
import yt_dlp
from googlesearch import search 
from tqdm import tqdm

def clean_cookie():
	if os.path.exists(".google-cookie"):
		os.remove(".google-cookie")

homeFolder = os.path.abspath(os.getcwd() + "\\songs")
os.chdir(homeFolder)
clean_cookie()

i=0
for filename in glob.iglob(homeFolder + "/**/song.ini", recursive=True):
	i+=1

with tqdm(total=i,unit="videos") as pbar:
	for filename in glob.iglob(homeFolder + "/**/song.ini", recursive=True):
		currentSongFileFolder = os.path.dirname(filename)
		currentSongName = os.path.basename(currentSongFileFolder)
		os.chdir(currentSongFileFolder)
		time.sleep (0.0001)
		pbar.update(1)

		if not os.path.exists("video.mp4"):
			query = 'Youtube {} (Official Music Video)'.format(currentSongName)

			# scrapes the URL from google
			for j in search(query, tld="com", lang='en', num=1, start=0, stop=1):
				url = j;

			# downloads the song
			ydl_opts = {'outtmpl': 'video.mp4',
					'format': 'mp4',
					'nooverwrites': 0,
					'noplaylist': 1,
					'quiet': True}
			with yt_dlp.YoutubeDL(ydl_opts) as ydl:
				ydl.download([url])

			# change the song.ini file to attempt to sync the video
			config = configparser.ConfigParser()
			config.read('song.ini')
			config.set('song', 'video_start_time', '-3000')

			with open('song.ini', 'w') as configfile:
				config.write(configfile)

			clean_cookie()