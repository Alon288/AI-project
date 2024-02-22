import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import webbrowser
from keyboard import press
from keyboard import press_and_release
from keyboard import write
import cv2
import sys

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    try:
        with sr.Microphone(device_index=2) as source:
            print('listening...')
            voice = listener.listen(source)
            print(voice)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'cortana' in command:
                command = command.replace('cortana', '')
                print(command)
    except:
        pass
    return command


def run_cortana():
    command = take_command()
    print(command)
    query = str(command)
    if 'play' in command: ## playing video on youtube ##
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'time' in command: ## Time telling ##
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)
    elif 'tell me about' in command: ## Wikipedia searching ##
        person = command.replace('tell me about', '')
        info = wikipedia.summary(person, 10)
        print(info)
        talk(info)
    elif 'date' in command: ## telling date ##
        talk('sorry, I have a headache')
    elif 'joke' in command: ## cracking joke ##
        talk(pyjokes.get_joke())
    elif 'open google' in command: ## opening google or any other website ##
        webbrowser.open("https://www.google.com")
    #elif 'search on google' in command:
    #    command = command.replace("search on google", "")
    #    webbrowser.open(f"https://www.google.com/search?q={command}")
    elif 'open flex' in command:
        webbrowser.open("https://flexstudent.nu.edu.pk/Login")
    elif 'open chat gpt' in command:
        webbrowser.open("https://chat.openai.com")
    elif 'open new tab' in query:
        press_and_release('ctrl + t')
    elif 'open youtube' in command:
        webbrowser.open("https://www.youtube.com")
    elif 'search on youtube' in command:
        command = command.replace("search on youtube", "")
        webbrowser.open(f"https://www.youtube.com/results?search_query={command}")
    #elif 'close tab' in query:
    #    press_and_release('ctrl + w')
    # elif 'new window' in query:
    #    press_and_release('ctrl + n')
    #elif 'download' in query:
    #    press_and_release('ctrl + j')
    #elif 'history' in query:
    #    press_and_release('ctrl + h')
    # name = query.replace("open", "")
    # Name = str(name) 
    # string = "https://www." + Name + ".com"
    # web.open(string)
    elif 'open camera' in command: ## opening camera ##
        cap= cv2.VideoCapture(0)
        while True:
            ret, img =cap.read()
            cv2.imshow('webcam', img)
            k=cv2.waitKey(50)
            if k == 27:
                break;
        cap.release()
        cv2.destroyAllWindows()
    elif 'go to sleep' in command: ## turning off the agent ##
        talk('i am switching off')
        sys.exit()
    else:
        talk('Say that again please.')

while True:
    run_cortana()