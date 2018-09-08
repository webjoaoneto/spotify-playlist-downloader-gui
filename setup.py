from cx_Freeze import setup, Executable
import sys

base = 'Win32GUI'

executables = [Executable("index.py", base=base)]


includes = [
    'sys', 
    'spotipy',
    'encodings', 
    'PyQt5', "os", 'spotipy','googleapiclient']
packages = [ 'spotipy', 'time','threading', 'queue', 'idna','googleapiclient.discovery']
includefiles= [ 'ui/','tools/', 'actions/']

options = {
    'build_exe': {    
        'packages':packages,
        'includes': includes,
        'include_files':includefiles
    },
}

setup(
    name = "SpotiTube Downloader",
    options = options,
    version = "1.0.0",
    description = 'Download spotify musics from Youtube',
    executables = executables
)

