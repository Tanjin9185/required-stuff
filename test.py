import speech_recognition as sr 
from time import ctime 
import time
import webbrowser
import os 
import playsound 
import random
from gtts import gTTS
from threading import Thread
r = sr.Recognizer()

bangla_book="/home/rahi/Desktop/Books/bangla/"

def chapter():
        playing=True

        os.system(f'vlc-ctrl play -p {bangla_book}/chapter1.mp4')

def open():
    os.system(f'nautilus {bangla_book}')

 
def record_audio(ask=False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        voice_data=""
        try:
            voice_data = r.recognize_google(audio)
        except sr.UnknownValueError:
            speak('Sorry, I did not get that')
        except sr.RequestError:
            speak('Sorry, my speech service is down,Check your Internet connection.')

        return voice_data.lower()

def speak(text):
    tts =gTTS(text=text,lang='en')
    r=random.randint(1,100000000)
    audio_file='audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(text)
    os.remove(audio_file)

def response(voice_data):
    playing=False
    if 'what is your name' in voice_data:
        speak('My name is Spac')

    if 'what time is it' in voice_data:
        speak(ctime())
    
    if 'search' in voice_data:
        search = record_audio('what do you want to search for ?')
        url = "https://google.com/search?q="+search 
        webbrowser.get('firefox').open_new_tab(url)
        speak("Here is what is found for "+search)

    if 'find' and 'location' in voice_data:
        location = record_audio("What is the location?")
        url = 'http://google.nl/maps/place/'+location+'/&amp;'
        webbrowser.get('firefox').open_new_tab(url)
        speak("Here is the location of " + location)


        if "close" in voice_data:
            speak('closing tab')
            webbrowser.close()
    if 'open' and 'bangla' in voice_data:
        speak("Opening bangla book")
        Thread(target=open).start()
        ask = record_audio("which Chapter?")
        if "chapter on" in ask or "chapter 1" in ask or "chapter one" in ask or "1" in ask or "one" in ask:
            speak('Chapter one is playing')
            Thread(target=chapter).start()
    if playing == True:
        if "pause" in voice_data:
            os.system(f'vlc-ctrl pause')
        if 'play' in voice_data:
            os.system(f'vlc-ctrl play')
        if 'volume' and 'up' in voice_data:
            os.system(f'vlc-ctrl volume +10%')
        if 'volume' and 'down' in voice_data:
            os.system(f'vlc-ctrl volume +0.1')
        if 'stop' in voice_data or 'quit' in voice_data:
            os.system(f'vlc-ctrl quit')
    if 'exit' in voice_data:
        speak("Good bye sir")
        exit()

    if "thanks" in voice_data or 'thank you' in voice_data:
        speak("You are also welcome")

    if "kamon" in voice_data or 'kemon' in voice_data:
        speak("ami bhalo ashi,apni kamon ashen?")
    
    if 'kobita' in voice_data:
        speak('oi dakha jay tal gash,oi amader gah,shei khanete bash kore kana bogir shaa')

time.sleep(1)    
speak("How can I help you?")

while 1: 
    voice_data = record_audio()
    print(voice_data)
    response(voice_data)