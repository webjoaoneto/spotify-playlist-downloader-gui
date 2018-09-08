# Spotify Playlist Downloader

This is an **SIMPLE** but usefull gui -- Written in Python with PyQT5 -- to export an entire spotify playlist to mp3 - Using Youtube.


# How it works

* Get the Spotify Playlists song list via Spotify API
* Search each song for the Youtube video related (Search for Artist + Trackname )
* And finaly uses youtube-dl.exe to extract youtube video to mp3

## Running steps

* we have a few steps to configure everything
1 - Download this repo
2 - Ensure that you have python 3.5 or greater installed and running on our PC
3 - Run this commands
	`pip install -r requirements.txt`
	`python.exe index.py`
4 - Or try to use our compiled exe version from here (Windows 10 only): 
	--link--
	
## Screenshots
![Print](https://image.ibb.co/kEbX79/print1.png)

## REQUIRED: Youtube-dl and ffmpeg binaries

**IMPORTANT**:
This program to work need ffmpeg and youtube-dl binaries to convert youtube videos to mp3.
Please download and put ffmpeg.exe and youtube-dl.exe into the path
`projectFolder/tools/`

[Youtube-dl Download link](https://rg3.github.io/youtube-dl/download.html) 
-> Must be in: `projectFolder/tools/youtube-dl.exe`

[Fffmpeg download links](https://ffmpeg.zeranoe.com/builds/)
-> Must be in: `projectFolder/tools/ffmpeg.exe`
Your project path must be like that:

## BUGS AND ISSUES
Be free to send bugs or improve this program.
