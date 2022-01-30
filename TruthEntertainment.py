import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.config import Config
from kivy.uix.button import Button
from kivy.uix.label import Label

import playsound
import speech_recognition as sr
import hack3
import multiprocessing
from pygame import mixer
from gtts import gTTS
import time
import os
import hack3
import HackathonProgram3 as p

Builder.load_file('MainMenu.kv')

def txt_to_speech(ebook_name):
    text = fileToString(ebook_name)
    text_split = text.split("\n\n")
    count = 0
    queueList = []
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


def getBooks():
        path = os.getcwd()
        
        os.chdir(path)
        
        booklist = []
        for file in os.listdir():
           if file.endswith('.txt'):
              booklist.append(file)
        return booklist
audiobooks = getBooks()

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


class Launch(FloatLayout):
    
    def __init__(self, **kwargs):
        super(Launch, self).__init__(**kwargs)
        self._keyboard = Window.request_keyboard(self._keyboard_closed, self)
        self._keyboard.bind(on_key_down=self._on_keyboard_down)
        self.createMainWindow()
        
    def _keyboard_closed(self):
        self._keyboard.unbind(on_key_down=self._on_keyboard_down)
        self._keyboard = None

    def saycurrentbook(self):
        if self.currentbook == 0:
            self.ChooseBook1()
            
        elif self.currentbook == 1:
            self.ChooseBook2()
            
        elif self.currentbook == 2:
            self.ChooseBook3()

    def _on_keyboard_down(self, keyboard, keycode, text, modifiers):
        if keycode[1] == 'up':
            if self.currentbook == 0:
                self.currentbook = 0
            else:
                self.currentbook -= 1
            self.saycurrentbook()
        elif keycode[1] == 'down':
            if self.currentbook == 2:
                    self.currentbook = 2
            else:
                self.currentbook += 1
            self.saycurrentbook()
            
        #---------------------------------FIXME----------------------------------#
        # Get it to play the audio/words in a text file
            
        elif keycode[1] == 'p':
            self.currentfile = audiobooks[self.currentbook]  #textfile
            
            x = p.fileToString(self.currentfile)
            p.speak(x)
            
            """
            this_filename = self.currentfile.replace(".txt", "")
            tts.save(this_filename + '.mp3')
            mixer.music.load(this_filename + '.mp3')
            mixer.music.play()
            
            while(1):
                #print(mixer.music.get_busy())
                if (not(mixer.music.get_busy())):
                    break
            
            
        """
        return True
        #---------------------------------FIXME----------------------------------#

    def StartupVoice(self):
        mixer.init()
        text = "Welcome to Truth Entertainment System, which of these audio books would you like to listen to? Press the down and up keys to cycle through the available books, and press enter to select that book" 
        tts = gTTS(text=text, lang='en')
        
        this_filename = 'abc6'
        tts.save(this_filename + '.mp3')
        mixer.music.load(this_filename + '.mp3')
        mixer.music.play()
        
        while(1):
            #print(mixer.music.get_busy())
            if (not(mixer.music.get_busy())):
                break
            
    def ChooseBook1(self):
        mixer.init()
        self.currentbook = 0
        text = "Book 1, Romeo and Juliet"
        tts = gTTS(text=text, lang='en')
        
        this_filename = 'book1'
        tts.save(this_filename + '.mp3')
        mixer.music.load(this_filename + '.mp3')
        mixer.music.play()
        
        while(1):
            #print(mixer.music.get_busy())
            if (not(mixer.music.get_busy())):
                break
            
    def ChooseBook2(self):
        mixer.init()
        self.currentbook = 1
        text = "Book 2, The Giver"
        tts = gTTS(text=text, lang='en')
        
        this_filename = 'book2'
        tts.save(this_filename + '.mp3')
        mixer.music.load(this_filename + '.mp3')
        mixer.music.play()
        
        while(1):
            #print(mixer.music.get_busy())
            if (not(mixer.music.get_busy())):
                break
            
    def ChooseBook3(self):
        mixer.init()
        self.currentbook = 1
        text = "Book 3, The Hunger Games"
        tts = gTTS(text=text, lang='en')
        
        this_filename = 'book3'
        tts.save(this_filename + '.mp3')
        mixer.music.load(this_filename + '.mp3')
        mixer.music.play()
        
        while(1):
            #print(mixer.music.get_busy())
            if (not(mixer.music.get_busy())):
                break


    def createMainWindow(self):
        self.MainTitle = Label(
            text="Truth Entertainment",
            font_size= 80,
            color= (1,1,1,1),
            size_hint = (0.25,0.2) ,
            pos_hint = {"x":0.38, "y":0.5})
        self.add_widget(self.MainTitle)

        self.DirectoryButton = Button(
            text="Search Local \n     Storage",
            font_size= 40,
            color= (1,1,1,1),
            size_hint= (0.6,0.15),
            pos_hint= {"x" : 0.2, "y" : 0.2})
        self.add_widget(self.DirectoryButton)
        self.DirectoryButton.bind(on_press=self.DirectoryPress)
        self.currentbook = 0
        
    def destroyMainWindow(self):
        self.remove_widget(self.DirectoryButton)
        self.remove_widget(self.MainTitle)
    
    def createWindowTwo(self):
        self.Book1 = Label(
            text = f"1) {audiobooks[0]}",
            font_size= 45,
            color= (1,1,1,1),
            size_hint = (0.25,0.2) ,
            pos_hint = {"x":0.4, "y":0.8})
        self.add_widget(self.Book1)
        
        self.Book2 = Label(
            text = f"2) {audiobooks[1]}",
            font_size= 45,
            color= (1,1,1,1),
            size_hint = (0.25,0.2) ,
            pos_hint = {"x":0.4, "y":0.7})
        self.add_widget(self.Book2)
        
        self.Book3 = Label(
            text = f"3) {audiobooks[2]}",
            font_size= 45,
            color= (1,1,1,1),
            size_hint = (0.25,0.2) ,
            pos_hint = {"x":0.4, "y":0.6})
        self.add_widget(self.Book3)
        
    
    def destroyWindowTwo(self):
        self.remove_widget(self.NewTitle)
        self.remove_widget(self.NextListen)
    
        
    
    def DirectoryPress(self, instance):
        self.destroyMainWindow()
        self.createWindowTwo()
        #self.StartupVoice()

        

class App(App):
    def build(self):
        return Launch()


if __name__ == "__main__":
    #Window.fullscreen = "auto"
    print(audiobooks)
    App().run()
    
    
