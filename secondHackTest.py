from gtts import gTTS
import os
import playsound
import speech_recognition as sr
import hack3
import multiprocessing
from pygame import mixer
import time

def fileToString(fileName):
    with open(fileName, 'r', encoding="utf8") as f:
        read_data = f.read()
    f.close()
    return read_data

def my_listenQuick():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source, None, 2) 
            
        
        try:
            #print("You said " + r.recognize_google(audio))
            return r.recognize_google(audio)
        except sr.UnknownValueError:
           print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
            
def my_listen():
        r = sr.Recognizer()                                                                                   
        with sr.Microphone() as source:                                                                       
            print("Speak:")                                                                                   
            audio = r.listen(source, None, 3) 
            
        
        try:
            #print("You said " + r.recognize_google(audio))
            return r.recognize_google(audio)
        except sr.UnknownValueError:
           print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))

mixer.init()
text = "Which audio book would you like to listen to?"
tts = gTTS(text=text, lang='en')

this_filename = 'abc6'
tts.save(this_filename + '.mp3')
mixer.music.load(this_filename + '.mp3')
mixer.music.play()

while(1):
    #print(mixer.music.get_busy())
    if (not(mixer.music.get_busy())):
        break

mixer.music.unload()
#mixer.music.queue(this_filename + '.mp3')
queueList = []
#queueList.append(this_filename + '.mp3')
chosenBook = my_listen()
book_file = hack3.getTextFile(chosenBook)
text = fileToString("facebook.txt")
text_split = text.split("\n\n")
count = 0
for segment in text_split:
    if (count > 20):
        break
    #if (count < 8):
        #count += 1
     #   continue
    try:
        print(count)
        text = segment
        tts = gTTS(text=text, lang='en')
        
        this_filename = 'file' + str(count)
        tts.save(this_filename + '.mp3')
        count += 1
        
        queueList.append(this_filename + '.mp3')
    except:
        x = 0

count = 0
paused = False
while(1):
    if (not(mixer.music.get_busy()) and count < len(queueList) and (not paused)):
        mixer.music.unload()
        mixer.music.load(queueList[count])
        mixer.music.play()
        count += 1
    response = my_listenQuick()
    if (response == 'pause'):
        mixer.music.pause()
        paused = True
    if (response == 'play'):
        mixer.music.unpause()
        paused = False
    
    
    

while(1):
    #print(mixer.music.get_busy())
    if (not(mixer.music.get_busy())):
        break


mixer.music.queue(this_filename + '.mp3')
mixer.music.unload()
os.remove(this_filename + '.mp3')