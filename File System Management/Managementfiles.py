# organize the desktop
# moves images, videos, screenshots, and audio files
# into corresponding folders
import os
import shutil
from pathlib import Path


audio = (".3ga", ".aac", ".ac3", ".aif", ".aiff",
         ".alac", ".amr", ".ape", ".au", ".dss",
         ".flac", ".flv", ".m4a", ".m4b", ".m4p",
         ".mp3", ".mpga", ".ogg", ".oga", ".mogg",
         ".opus", ".qcp", ".tta", ".voc", ".wav",
         ".wma", ".wv")

video = (".webm", ".MTS", ".M2TS", ".TS", ".mov",
         ".mp4", ".m4p", ".m4v", ".mxf")

img = (".jpg", ".jpeg", ".jfif", ".pjpeg", ".pjp", ".png",
       ".gif", ".webp", ".svg", ".apng", ".avif")

excel = (".xlsx",".xlsm",".xlsb",".xls", ".xml")

desktop = (".bat", ".exe", ".lnk")

sql = (".sql")

def is_audio(file):
    return os.path.splitext(file)[1] in audio

def is_video(file):
    return os.path.splitext(file)[1] in video

def is_image(file):
    return os.path.splitext(file)[1] in img

def is_screenshot(file):
    name, ext = os.path.splitext(file)
    return (ext in img) and "screenshot" in name.lower()

def is_excel(file):
    return os.path.splitext(file)[1] in excel

def is_desktopfile(file):
    return os.path.splitext(file)[1] in desktop

def is_sql(file):
    return os.path.splitext(file)[1] in sql


os.chdir("C:/Users/mlpradhan/OneDrive - alliedelec.com/Desktop")

pathfolder = "C:/Users/mlpradhan/OneDrive - alliedelec.com/Documents/Files"


for file in os.listdir():
    if is_audio(file):
        shutil.move(file, pathfolder + "/audio")
    elif is_video(file):
        shutil.move(file, pathfolder + "/video")
    elif is_image(file):
        if is_screenshot(file):
            shutil.move(file, pathfolder + "/screenshots")
        else:
            shutil.move(file, pathfolder + "/images")
    elif is_excel(file):
        shutil.move(file, pathfolder + "/excel")
    elif is_sql(file):
        shutil.move(file, pathfolder + "/SQL Statements")
    elif is_desktopfile(file):
         continue
    else:       
        fullpath = Path("C:/Users/mlpradhan/OneDrive - alliedelec.com/Documents/Files/Other_Folders/" + file)    
        if fullpath.exists():
           os.remove(fullpath)
           shutil.move(file,  "C:/Users/mlpradhan/OneDrive - alliedelec.com/Documents/Files/Other_Folders" )
        else:   
            shutil.move(file, "C:/Users/mlpradhan/OneDrive - alliedelec.com/Documents/Files/Other_Folders")
