from tkinter import*
import time;
import random
import tkinter.messagebox
from PIL import Image
from tkinter import*
import os
#import wolframalpha,os
import speech_recognition as sr
import pyttsx3
import io
from tkinter import ttk
import base64
import turtle
import pyaudio
from pygame import mixer
import webbrowser
from time import localtime,strftime
import time

from tkinter import *   ## notice lowercase 't' in tkinter here
from urllib.request import urlopen
from urllib.request import urlopen
import _thread
from tkinter import font
from tkinter import messagebox
import socket
import time
import select
import queue
import pocketsphinx
import threading

 

def voice_command():
       # try:





                window5=Tk()
                window5.configure(background="steel Blue")
                window5.title("Artificial Intellegence - Icecream")
                #window5.state('zoomed')
                #________________________________calling function____________________
                def quit():
                        window5.destroy()
                        return

                def update_text(userinput_text):
                        print ("update text")
                        print("your turn")
                        label_input['text']=userinput_text

                def get_answer(question):
                        def speak(text):
                            engine = pyttsx3.init()
                            engine.say(text)
                            update_text(text)
                            engine.runAndWait()



                        app_id='' # wolframalpha app ID



                        if ("restart") in question:
                            pass

                        if ("exit") in question:

                                rand = ['Goodbye Sir', 'Icecream powering off in 3, 2, 1, 0']
                                speak(rand)
                                quit()
                        if ('hello') in question or ('hi') in question:
                                rand = ('Wellcome to icecream intelligence project. At your service sir.')
                                speak(rand)
                        if ('thanks') in question or ('tanks') in question or ('thank you') in question:
                                    rand = ['You are wellcome', 'no problem']
                                    speak(rand)
                        if  ("ice cream") in question or("icecream")in question or ("Icecream")in question:

                                speak('Yes Sir? ,What can I doo for you sir?')

                        if  ('how are you') in question or ('and you') in question or ('are you okay') in question:
                                    rand = ['Fine thank you']
                                    speak(rand)
                        if  ('*') in question:
                                    rand = ['Be polite please']
                                    speak(rand)
                        if ('your name') in question:
                                    rand = ['My name is Icecream, at your service sir']
                                    speak(rand)
                        if ('.com') in question :
                                    rahi = ['Opening' + question]
                                    speak(rahi)
                                    webbrowser.open_new_tab('http://www.'+question)
                                    print ('')
                        if ("who made you") in question or ("made") in question:
                            speak("Imran Hasan Rahi made me. He is my boss")
                        if ("tumi") in question or ("bangla") in question or ("Jano") in question:
                            speak("ha ,ami olpo olpo bangla jani, ami Bangla ke bhalobashi,Bangladesh Ke valobashi")
                        if ("have") in question or("girlfriend") in question:
                            speak("Still I am single, But I love roboot Sofia")
                            
                        if  ("where")  in question:
                                    query = question
                                    stopwords = ['google', 'maps']
                                    querywords = query.split()
                                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                                    result = ' '.join(resultwords)
                                    webbrowser.open_new_tab("https://www.google.be/maps/place/"+result+"/")
                                    rand = [result+'on google maps']
                                    speak(rand)
                        if ('install') in question:
                                    query = question
                                    stopwords = ['install']
                                    querywords = query.split()
                                    resultwords  = [word for word in querywords if word.lower() not in stopwords]
                                    result = ' '.join(resultwords)
                                    rand = [('installing '+result)]
                                    speak(rand)
                                    os.system('python -m pip install ' + result)
                        if ('sleep mode') in question:
                                    rand = ['good night']
                                    speak(rand)
                                    os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
                        if ('what time') in question:
                                    tim = strftime("%X", localtime())
                                    rand = [tim]
                                    speak(rand)
                        if  ("online") in question:
                                    speak("yes sir,Icecream is now in Active")
                                    speak("Starting all system application")
                                    speak("installing all divers")
                                    speak("every diver is installed")
                                    speak("all system have been started")
                                    speak("now I am online sir")
                        if ("Internet") in question:
                                internetexplorer()
                        if ("Firefox") in question:
                                    speak(" I heard you")
                                    speak("finding firefox application")
                                    speak("configuring all required files")
                                    speak("starting mozilla firefox")
                                    os.system("start firefox")
                        if ("Notepad") in question:
                                    speak("ok sir")
                                    speak("requested application is text editor")
                                    speak("joining required files")
                                    speak("starting notepad")
                                    os.system("start notepad.exe")
                        if ("python")in question:

                                    speak("start python.exe")
                                    speak("python is opening")
                                    os.system("start python.exe")

                        if ("find") in question:
                            speak("start chrome.exe")
                            speak("what do i search for you sir")
                            webbrowser.open_new_tab("http://google.com/?q=%s"%question)
                            speak("okay searching")
                        # if ("open") in question:
                        #         speak("opening gallary")
                        #         os.startfile("c:/users/zanja/Desktop/Icecream\dataSet")
                       






                        if question=="who are you" or question=="what is your name":
                                speak("I am Icecream, I am a Artificial Intellegence")
                        if question=="father"or question=="nation"or question=="who is the father of the nation":
                            speak(" Banga Bandhu Sheik Muzibur Rahman is the father of nation")

                        else:


                                try:

                                    client = wolframalpha.Client(app_id)
                                    res = client.query(question)
                                    for pod in res.pods:

                                        for sub in pod.subpods:
                                            print(sub)
                                                # print(next(res.results).text)
                                        print ('$$$$$$$$$$$$$$$$$$$$$$$')

                                        print(next(res.results).text)
                                        speak=next(res.results).text
                                except:
                                        speak("Say something")



                def audio():
                        doss=os.getcwd()

                        button_activate['text']="IceCream Activated."
                        button_activate['state']='disabled'
                        pb.start()
                        while True:
                                def speak(text):
                                    engine = pyttsx3.init()
                                    engine.say(text)
                                    update_text(text)
                                    engine.runAndWait()
                                    # Record Audio
                                r = sr.Recognizer()
                                with sr.Microphone() as source:
                                    audio = r.adjust_for_ambient_noise(source) #,duration=5

                                    print("Say something!")
                                   # speak("Welcome to Team IceCream Intellegence Project")
                                    userinput="Welcome to Team IceCream Intellegence Project"
                                   # speak("How can I help you , sir?")
                                    userinput="How can I help you,sir?"
                                    userinput= "Say Something..."
                                    update_text(userinput)
                                    audio = r.listen(source)

                                    # Speech recognition using Google Speech Recognition
                                try:

                                        # tanother API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`

                                    userinput=r.recognize_sphinx(audio)
                                    print("You said: " + userinput)
                                    update_text(userinput)

                                    get_answer(userinput)


                                except sr.UnknownValueError:
                                    print("Google Speech Recognition could not understand audio")
                                    userinput="Google Speech Recognition could not understand audio"
                                except sr.RequestError as e:
                                    print("Could not request results from Google Speech Recognition service; {0}".format(e))
                                    userinput="Could not request results from Google Speech Recognition service; {0}".format(e)
                                # update_text(userinput)
                def performanceBoost():
                                # update_text("Activating voice recognization...")
                        t1=_thread.start_new_thread( update_text, ("Say Something..", ) )
                        t2=_thread.start_new_thread( audio,())

                frame1=Frame(window5,height=330, width=660,borderwidth=2,relief=RIDGE,bg='#030719',highlightbackground='white')
                frame1.pack()
                frame1.place(relx=0.3, rely=0.4)

                label_input=Label(frame1, text="",font='Verdana 8 bold',fg='#0C90F2',bg='#030719', wraplength=600)
                label_input.pack(anchor=W)
                label_input.place(relx=0.5, rely=0.5, anchor=CENTER)


                button_activate=Button(window5,text="Activate",command=performanceBoost,width=15,justify='center',borderwidth=4,font='Verdana 8 bold')
                button_activate.pack(anchor=W)
                button_activate.place(relx=0.5, rely=0.2, anchor=CENTER)

                pb = ttk.Progressbar(frame1, orient="horizontal", length=660, mode="determinate")
                pb.pack()
                pb.place(rely=0.95)
                window5.mainloop()



        #except:
        #        messagebox.showinfo("Warning","First please secure Internet connection")
 
 
voice_command()
