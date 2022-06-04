Clone Hero Video Downloader
===========
A python script that allows you to download the top YouTube music video for songs in your Clone Hero library.


What this does
-------
This script will recursively run through your Clone Hero songs folder to find songs that are missing a video.mp4 file.  It will then search Google for the top youtube result for that song name (based on folder name), and then download that youtube video and place it in the directory.  Videos are downloaded without audio (to conserve space) and in the best possible quality (to make them look good).  The end result will be that when playing that song in Clone Hero, the background will be the music video of that song.

This script has been tested on very large song libraries with thousands of songs in many nested folders and has been found to be performant.  Please note that because most videos will download in 1080p resolution they can be up to 200MB per video.  The amount of time it takes to download videos for all of your songs will be highly dependant on your internet speed.  A progress bar is provided to indicate how many videos still need to be downloaded and will attempt to estimate the time remaining.

This script has also been designed to run multiple times on the same songs directory.  So, if you add new songs to Clone Hero, simply re-run the script and it will only download the videos that are missing.


Usage
-------
1. Extract into your Clone Hero directory
2. Run `pip install -r requirements.txt`
3. Run VideoDownload.py