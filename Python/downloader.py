from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from moviepy.editor import *
from pytube import YouTube
from pytube import Playlist

import pytube
import os
import moviepy.editor as mp
import re

from os import path
from pydub import AudioSegment


def pobieraniePlaylist():
    playlist = Playlist("") # Link do playlisty

        
    for url in playlist:
        print(url)
    
    for vid in playlist.videos:
        print(vid)

    # for url in playlist:
    #     YouTube(url).streams.filter(only_audio=True).first().download()


    for url in playlist:
        try:
            YouTube(url).streams.first().download("") # gdzie ma to zapisać
        except:
            print(f'błąd w:{url}')
            continue



    folder = "" # gdzie ma to zapisac

    for file in os.listdir(folder):
        if re.search('3gpp', file):
            mp4_path = os.path.join(folder,file)
            mp3_path = os.path.join(folder,os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)


def konwerterMp4ToMp3():
    

    mp4_file = r''
    mp3_file = r''

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()



def PobieranieFilmuYT():
    link = input('Wpisz link: ')
    yt = YouTube(link)

    #Title of video
    print('Tytul: ',yt.title)
    #Number of views of video
    print('Ilosc wyswietlen: ',yt.views)
    #Length of the video
    print('Dlugosc filmu: ',yt.length,'sekund')
    #Description of video
    print("Opis: ",yt.description)
    #Rating
    print("Oceny: ",yt.rating)

    print('Pobieram...')
    ys = yt.streams.get_highest_resolution()
    ys.download('') # gdzie ma to pobrac
    print('POBRANO!')


def PobieranieFilmuYTPetla():
    linkList = []
    print('Wpisz STOP jeśli chcesz zakonczyc wpisywanie linkow!')
    while True:

        link = input('Wpisz link: ')
        if link.upper() != 'STOP':
            if link in linkList:
                print('To juz było, coś innego daj!')
            else:
                linkList.append(link)
        
        else:
            break


    for linker in linkList:
        yt = YouTube(linker)
        #Title of video
        print('\n')
        print('Tytul: ',yt.title)
        #Number of views of video
        print('Ilosc wyswietlen: ',yt.views)
        #Length of the video
        print('Dlugosc filmu: ',yt.length,'sekund')
        #Description of video
        print("Opis: ",yt.description)
        #Rating
        print("Oceny: ",yt.rating)
        print('\n')

        print('Pobieram...')
        ys = yt.streams.get_highest_resolution()
        ys.download("") # gdzie ma to pobrac
        print('POBRANO!')



def KonwerMp3Wav():

  
   
    directory = "" # gdzie ma to pobrac
 
    for filename in os.scandir(directory):
        if filename.is_file():
            
            sound = AudioSegment.from_mp3(filename)

            nowaNazwa = str(filename).replace(".mp3", "")
            
            sound.export(nowaNazwa, format="wav")
    
    # convert mp3 file to wav file
    

#pdoaj funkcje