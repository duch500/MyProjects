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


##### PLAYLISTY ########

def Playlista():
    
    link = input("Podaj adres URL playlisty: ")
    droga = input("\nPodaj ścieżkę, gdzie chcesz zapisać playlistę: ")


    while True:
        res = input('\nCzy zależy Ci na wysokiej jakości obrazie (TAK/NIE):')

        if res.lower() == 'tak' or res.lower() == 'nie':
            break
        else:
            print('Podaj poprawną wartość \n')
            continue

    yt_playlist = Playlist(link)

    nieudanePobrania = []
    i = 1
    for video in yt_playlist.videos:
        try:

            if res.lower() == 'tak':
            
                video.streams.get_highest_resolution().download(output_path=droga, filename= " "+video.title+".mp4")
            else:
                video.streams.get_lowest_resolution().download(output_path=droga, filename= " "+video.title+".mp4")
            
            #Title of video
            print('\n')
            print('Tytul: ',video.title)
            #Number of views of video
            print('Ilosc wyswietlen: ',video.views)
            #Length of the video
            print('Dlugosc filmu: ',video.length,'sekund')
            print('\n')

            print('Pobieram...')
            print("Wideo pobrane: ", video.title ,'\n')
            i=i+1
            
       
        except:
            print(video.title + " ominięty\n")
            urlFilmu = video.watch_url
            print(f'Adres url: {urlFilmu}\n')
            nieudanePobrania.append(urlFilmu)
            pass
    print("\n Wszystkie możliwe wideo pobrane!.")

    if len(nieudanePobrania) != 0:
        
        while True:
            PobieraniePonowneCzy = input('\nCzy chcesz spróbować ponownie pobrać pomienięte filmy (TAK/NIE):')
            try:
                if PobieraniePonowneCzy.lower() == 'tak':
                    for video in nieudanePobrania:
                        yt = YouTube(video)
                        print('\n')
                        print('Tytul: ',yt.title)
                        #Number of views of video
                        print('Ilosc wyswietlen: ',yt.views)
                        #Length of the video
                        print('Dlugosc filmu: ',yt.length,'sekund')
                        print('\n')
                        print('Pobieram...')
                        if res.lower() == 'tak':
                            ys = yt.streams.get_highest_resolution()
                            
                        else:
                            ys = yt.streams.get_lowest_resolution()
                        
                        ys.download(droga)
                        print('POBRANO!')

                elif PobieraniePonowneCzy.lower() == 'nie':
                    print('\nW porządku!')
                    break
                else:
                    print('Podaj poprawną wartość \n')
                    continue
            except:
                print(video.title + " Nie udane pobranie\n")
                pass
    else:
        pass
    

 
 ####################################
            #KONWERTERY
 ####################################

def konwerterMp4ToMp3():
    print('''Instrukcja: 
          1.Uważnie podaj ścieżkę pliku mp4.
          2.Podaj ścieżkę i nazwę pliku wraz z rozszerzeniem mp3 PRZYKŁAD:
          G:\Testy\Alfons - Ganjaman (MIKE EMILIO REMIX).mp4
          G:\Testy\Alfons - Ganjaman (MIKE EMILIO REMIX).mp3''')
    mp4_file = input("Podaj ścieżkę do pliku MP4: ")
   
    try:
        videoclip = VideoFileClip(mp4_file)
    except FileNotFoundError:
        print("Podana ścieżka jest nieprawidłowa lub plik nie istnieje.")
        exit()

    mp3_file = input("Podaj ścieżkę, pod którą chcesz zapisać plik MP3: ")

    videoclip = VideoFileClip(mp4_file)

    audioclip = videoclip.audio
    audioclip.write_audiofile(mp3_file)

    audioclip.close()
    videoclip.close()
    
    print('Konwertowanie zakończone pomyślnie!')

def KonwerMp3Wav():

    print('''Instrukcja: 
          1.Uważnie podaj ścieżkę pliku mp4.
          2.Podaj ścieżkę i nazwę pliku wraz z rozszerzeniem mp3 PRZYKŁAD:
          G:\Testy\Alfons - Ganjaman (MIKE EMILIO REMIX).mp4
          G:\Testy\Alfons - Ganjaman (MIKE EMILIO REMIX).mp3\n''')

    mp3_file = input('Ścieżka do pliku audio mp3: ')

   
    wav_file = input('Ścieżka do pliku audio wav gdzie chcesz dać: ')

    audio = AudioSegment.from_mp3(mp3_file)

    audio.export(wav_file, format="wav")
    

    print("Konwersja zakończona pomyślnie!")

    
    
 
            
            

 ####################################
            #FILMIKI
 ####################################


def Filmik():
    link = input("Podaj adres URL filmu: ")
    droga = input("\nPodaj ścieżkę, gdzie chcesz zapisać film: ")

    while True:
        res = input('\nCzy zależy Ci na wysokiej jakości obrazie (TAK/NIE):')

        if res.lower() == 'tak' or res.lower() == 'nie':
            break
        else:
            print('Podaj poprawną wartość \n')
            continue

    if res.lower() == 'tak':
            
        video = YouTube(link)
        highres = video.streams.get_highest_resolution()
        highres.download(droga)
    else:
        video = YouTube(link)
        lowhres = video.streams.get_lowest_resolution()
        lowhres.download(droga)
                
            
        #Title of video
        print('\n')
        print('Tytul: ',video.title)
        #Number of views of video
        print('Ilosc wyswietlen: ',video.views)
        #Length of the video
        print('Dlugosc filmu: ',video.length,'sekund')
        print('\n')

        print('Pobieram...')
        print("Wideo pobrane: ", video.title ,'\n')
    pass

def PobieranieFilmuYTPetla():
    linkList = []
    droga = input("\nPodaj ścieżkę, gdzie chcesz zapisać film: ")
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
        print('\n')
        print('Tytul: ',yt.title)
        print('Ilosc wyswietlen: ',yt.views)
        print('Dlugosc filmu: ',yt.length,'sekund')
        print('\n')
        print('Pobieram...')
        ys = yt.streams.get_highest_resolution()
        ys.download(droga)
        print('POBRANO!')







while True:

    st_dec = input('Chcesz pobrać playlistę czy filmik czy przekonwertować plik (P/F/K): ')
    if st_dec.lower() == 'p':
        Playlista()
        break

    elif st_dec.lower() == 'f':

        while True:
            decyFi = input('Czy chcesz jeden film pobrać czy więcej (J/W): ')

            if decyFi.lower() == 'j':
                Filmik()
                break
            elif decyFi.lower() == 'w':
                PobieranieFilmuYTPetla()
                break
            else:
                print('Podaj poprawną wartość \n')
                continue
        break
        


    elif st_dec.lower() == 'k':

        while True:
            decyFi = int(input('1. Konwerter mp4 -> mp3 \n 2.Konwerter mp3 -> wav \n Podaj numer: '))

            if decyFi == 1:
                konwerterMp4ToMp3()
                break
            elif decyFi == 2:
                KonwerMp3Wav()
                break
            else:
                print('Podaj poprawną wartość \n')
                continue
        
        break

    else:
        print('Podaj poprawną wartość!\n')
        continue
    


