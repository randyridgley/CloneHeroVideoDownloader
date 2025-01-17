<img src="https://github.com/jshackles/CloneHeroVideoDownloader/raw/master/assets/icon.png" width="32" height="32"></img> Clone Hero Video Downloader
===========
An application that allows you to download the top YouTube music video for songs in your Clone Hero library.


What this does
-------
This program will recursively run through your Clone Hero songs folder to find songs that are missing a video.mp4 file.  It will then search Google for the top YouTube result for that song name (based on folder name), and then download that YouTube video and place it in the directory. The end result will be that when playing that song in Clone Hero, the background will be the music video of that song.

This program has been tested on very large song libraries with thousands of songs in many nested folders and has been found to be performant.  Please note that because most videos will download in 1080p resolution they can be up to 200MB per video.  The amount of time it takes to download videos for all of your songs will be highly dependent on your internet speed.  A progress bar is provided to indicate how many videos still need to be downloaded and will attempt to estimate the time remaining.

This program has also been designed to run multiple times on the same songs directory.  So, if you add new songs to Clone Hero, simply re-run the program and it will only download the videos that are missing.


Usage
-------
1. [Download the latest release](https://github.com/jshackles/CloneHeroVideoDownloader/releases/latest)
2. Place VideoDownload.exe in your Clone Hero directory
3. Run VideoDownload.exe