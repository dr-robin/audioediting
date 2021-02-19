from moviepy.editor import *

def mp4files():
	x=glob.glob("../train/*.mp4")

def getaudio(mp4file):
	videoclip = VideoFileClip(mp4file)
	audioclip = videoclip.audio
	mp3file = mp4file.strip("mp4").join("mp3")
	audioclip.write_audiofile(mp3file)
	audioclip.close()
	videoclip.close()
