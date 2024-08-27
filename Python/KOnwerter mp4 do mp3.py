
from moviepy.editor import *
import os

# # Load the mp4 file
# video = VideoFileClip("example.mp4")

# # Extract audio from video
# video.audio.write_audiofile("example.mp3")

directory = "" # # gdzie ma to pobrac

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)

    if os.path.isfile(f):
        print("ŁADUJE", f)
        video = VideoFileClip(f)
        print('WIDEO ZALADOWANE', f)
        video.audio.write_audiofile(filename.replace("mp4", "mp3"))
        print("\n PRZEKONWERTOWANO", f, "\n")