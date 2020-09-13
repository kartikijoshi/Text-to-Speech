from gtts import gTTS
import os

f = open("text.txt",'r')

s = f.readlines()
f.close()
text=''
for lines in s:
	text=text+lines
language = 'en'
print("Please wait while we convert your file.")
try:
	audio = gTTS(text,lang=language,slow=False)
except:
	print("Sorry| This file cannot be converted.")
try:
	audio.save('audio.mp3')
except:
	print("Sorry| There was an error saving the audio file.")
print("All went well! File is converted.")