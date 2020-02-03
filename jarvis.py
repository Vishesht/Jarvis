import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice',voices[0].id)
#print(voices[0].id)          #show id of speaker
def speak(audio):
    print("Jarvis : ",audio)
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning")
    elif hour>=12 and hour<18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")
    speak("Hello Sir, I am Jarvis your assistant.  Please tell me how may i help you?")
def takecommand():
    #it takes microphone as input
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio,language = 'en-in')
            print("User said : {}".format(query))

        except:
            print("Say that again...")
            return "None"
        return query

def sendEmail(to,content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('pythonlang0@gmail.com','Lenovok8+')
    server.sendmail('visheshtg57@gmail.com',to,content)
    server.close()


def lib():
    while True:
        query = takecommand().lower()
        #logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('youtube.com')

        elif 'play music' in query:
            music_dir = 'D:\\MUSIC\\new fav 1'
            songs = os.listdir(music_dir)
            speak("Sir enjoy the music")
            print(songs)
            os.startfile(os.path.join(music_dir,random.choice(songs)))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print(strTime)
            speak(f"Sir, the time is {strTime}")
        elif 'open chrome' in query:
            codePath = r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
            os.startfile(codePath)
        elif 'send email' in query:
            try:
                speak("what should i say?")
                content = takecommand()
                to = "visheshtg57@gmail.com"
                sendEmail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry bose email was not sent!")
        elif "Make a reminder for me" in query:
            speak("whats the reminder sir")
#*******************Chatting***********************************************
        elif 'listen me' in query:
            speak("yes sir, please")
        elif "hello jarvis" in query:
            speak('Hello Sir! How are you?')
        elif "how are you" in query or "how's you" in query:
            speak('i am fine sir, what about yourself')
        elif "i am good" in query or "i am fine" in query:
            speak('good, Its nice to hear that')
        elif "i am getting bored" in query:
            speak('would you like to listen music,if yes then say play music')
        elif "tell me a joke" in query:
            speak('I dreamed, I was forced to eat a giant marshmallow. When I woke up, my pillow was gone.')
        elif "who i am" in query:
            speak('sir, your name is vishesht gupta, and you are a soul')
        elif "who is abhishek" in query:
            speak("abhish is your friend")
        elif "whats my future planning" in query:
            speak("its hard to know but i guess you will be a traveller")
        elif "my favourite phone brand" in query:
            speak("apple")
        elif "my timetable" in query:
            speak("""you wake up at 5Am, then you meditate for one hour,after that you are doing yoga for one hour
            At 7 and 7:30 you have to take medicine after that you are taking breakfast
            then its time to go for python tranning, at 7pm you go with friends for chillout 
             and at 11pm you go to bed for sleep""")
        elif "need to buy" in query:
            speak("white shoes,panjama kurta,glasses,watch and tshirts")
        elif "what to do" in query:
            speak("please make you assistant more powerful by doing editing inside the code")

#*******************Birthday************
        elif "when my bith date " in query:
            speak("its 10 august 1999")
        elif "whats abhishek birth date" in query:
            speak("its 9 august 1999")
        elif "gareema birthday" in query:
            speak("its 22 june")
        elif "when my mother birthday" in query:
            speak("23 december ")
        elif "when my grandmother birthday" in query:
            speak("on 23 december 1943")

#*******************phone number******************
        elif "Raghunandan phone number" in query:
            speak("its jio phone number is 7889794803")
        elif "shikhar phone number" in query:
            speak("7889466973")
        elif "abhishek phone number" in query:
            speak("7889358106")
        elif "sonu phone number" in query:
            speak("7992251613")
        elif "paarth phone number" in query:
            speak("7889947798")


#*******************************************

        elif "what i have learned" in query or "my knowlwdge" in query:
            speak("""you are best in html,css,python,tkinter,adobe after effects, adobe premium pro,photoshop,
            wordpress, django and you know the basic of java, c++ and you are a little bit hacker also by hacking cameras,
            wifi's            
            """)
        elif "my pending projects" in query:
            speak("The desire of all religions, agrisolution, woocommerce website, personal Jarvis,short video making")

        elif "ok bye jarvis" in query or "bye-bye" in query or "buy jarvis" in query or "bye jarvis" in query:
            speak("good Bye Sir, happy to help you, Have a good day")
            break

        elif "say hello to raghu" in query:
            speak("hello raghu how are you")

        elif "namaskar" in query:
            speak("namaskaar, tum kaise ho")

        if "where is" in query:
            data = query.split(" ")
            location = data[2]
            speak("Hold on Vishu, I will show you where " + location + " is.")
            os.system("chromium-browser https://www.google.nl/maps/place/" + location + "/&amp;")

if __name__ == '__main__':
    wishme()
    lib()