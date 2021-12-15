import os
from os import name, system, getenv, listdir
from os.path import isfile, join, basename
from colorama import Fore, init
import fileinput
import requests
import re
import json
import ctypes
from urllib.request import Request, urlopen
from watchdog.events import LoggingEventHandler
from watchdog.observers import Observer
import time
import shutil
import ctypes
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System, Box

banner = """
                    o
           o       /
            \     /
             \   /
              \ /
+--------------v-------------+
|  __________________      @ |
| /                  \       |
| |                  |  (\)  |
| |       Press      |       |
| |       Enter      |  (-)  |
| |                  |       |
| \                  / :|||: |
|  -ooo--------------  :|||: |
+----------------------------+
   []                    []
"""[1:]
Anime.Fade(Center.Center(banner), Colors.blue_to_purple, Colorate.Vertical, enter=True)

class WatchDogEvent (LoggingEventHandler):
    def on_created(self, event):
        document = os.path.expanduser("~")+"\Documents\\"
        image = os.path.isdir(f"{document}Images")
        video = os.path.isdir(f"{document}Videos")
        other = os.path.isdir(f"{document}Others")
        if ".jpg" in event.src_path or ".jpeg" in event.src_path or ".png" in event.src_path or ".apng" in event.src_path or ".avif" in event.src_path or ".gif" in event.src_path or ".svg" in event.src_path or ".webp" in event.src_path or ".bmp" in event.src_path or ".ico" in event.src_path or ".tiff" in event.src_path or ".jfif" in event.src_path or ".pjpeg" in event.src_path or "pjp" in event.src_path or ".cur" in event.src_path or ".tif" in event.src_path or ".webm" in event.src_path or ".mkv" in event.src_path or ".flv" in event.src_path or ".vob" in event.src_path or ".ogv" in event.src_path or ".ogg" in event.src_path or ".drc" in event.src_path or ".gifv" in event.src_path or ".mng" in event.src_path or ".avi" in event.src_path or ".mts" in event.src_path or "m2ts" in event.src_path or ".ts" in event.src_path or ".mov" in event.src_path or ".qt" in event.src_path or ".wmv" in event.src_path or ".yuv" in event.src_path or ".rm" in event.src_path or ".rmvb" in event.src_path or ".viv" in event.src_path or ".asf" in event.src_path or ".amv" in event.src_path or ".mp4" in event.src_path or ".m4p" in event.src_path or ".m4v" in event.src_path or ".mpg" in event.src_path or ".mp2" in event.src_path or ".mpeg" in event.src_path or ".mpe" in event.src_path or ".mpv" in event.src_path or ".m2v" in event.src_path or ".m4v" in event.src_path or ".svi" in event.src_path or ".3gp" in event.src_path or ".3g2" in event.src_path or ".mpv" in event.src_path or ".svi" in event.src_path or ".mxf" in event.src_path or ".roq" in event.src_path or ".nsv" in event.src_path or ".f4v" in event.src_path or ".f4p" in event.src_path or ".f4a" in event.src_path or ".f4b": 
            if ".jpg" in event.src_path: ### Parti Image
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".jpeg" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".apng" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".avif" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".gif" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".svg" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".webp" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".bmp" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".ico" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".tiff" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".jfif" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".pjpeg" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".pjp" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".cur" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".tif" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".png" in event.src_path:
                if image == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Images\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Images')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Images/' + basename(event.src_path))
            if ".webm" in event.src_path: ### Parti Videos
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mkv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".flv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".vob" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".ogv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".ogg" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".drc" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".gifv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mng" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".avi" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mts" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".m2ts" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".ts" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mov" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".qt" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".wmv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".yuv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".rm" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".rmvb" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".viv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".asf" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".amv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mp4" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".m4p" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".m4v" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mpg" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mp2" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mpeg" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mpe" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mpv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".m2v" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".m4v" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".svi" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".3gp" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".3g2" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".mxf" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".roq" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".nsv" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".f4v" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".f4p" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".f4a" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
            if ".f4b" in event.src_path:
                if video == True:
                    time.sleep(1)
                    shutil.move(event.src_path, document + 'Videos\\' + basename(event.src_path))
                else:
                    os.mkdir(document + 'Videos')
                    time.sleep(1)
                    os.rename(event.src_path, document + 'Videos/' + basename(event.src_path))
        else:
            if other == True:
                time.sleep(1)
                shutil.move(event.src_path, document + 'Others\\' + basename(event.src_path))
            else:
                os.mkdir(document + 'Others')
                time.sleep(1)
                os.rename(event.src_path, document + 'Others/' + basename(event.src_path))







def main():
    print(Fore.BLUE + " ")
    path = os.path.expanduser("~")+"\Downloads\\"
    print(Box.Lines(Fore.BLUE + "Bienvenue sur le Gestionnaire de fichier"))
    observer = Observer()
    observer.schedule(WatchDogEvent(), path, recursive=True)
    print(" ")
    print(Fore.WHITE + "[" + Fore.GREEN + "i" + Fore.WHITE + "]" + Fore.MAGENTA +" Gestionnaire de fichier actif.")
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

main()