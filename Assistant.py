import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
   
def wishMe():
    hour= int(datetime.datetime.now().hour)
    
    if hour>=0  and hour<12:
        speak("Good Morning!")
    elif hour>=12 and hour<17:
        speak("Good Afternoon!")
    else:
        speak("Good evening sir")
    speak("I am Siri . Please tell me how may i help you")

def takeCommand():
    """
    it takes microphone input from user and returns string output
    """
    try:
        r= sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)
    except Exception as e:
        print("sorry, please say that again")

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said : {query}\n")
    except exception as e:
        print("say that again please...")
        return "None"

    return query
def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls
    server.login("mayankramani9893@gmail.com","galaxyj7#")
    server.sendmail("mayankramani9893@gmail.com",to,content)
    server.close()


if __name__ == "__main__":
   # speak("vani is good")
    wishMe() 
    
    while True:

        query = takeCommand().lower()

        #logic for execting tasks based on query
        if 'wikipedia' in query:
            query=query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia ")
            print(results)
            speak(results)
        elif 'url' in query:
            url=query.split().pop()
            webbrowser.open(url)
        elif 'open youtube' in query:
            webbrowser.open("www.youtube.com")
        elif 'open google' in query:
            query1=query.split()
            webbrowser.open("www.google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("www.stackoverflow.com")
        elif 'open whatsapp' in query:
            webbrowser.open("https://web.whatsapp.com/")
        elif 'play music' in query:
            music_dir = 'F:\\english luv'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'open code' in query:
            codePath = "C:\\Users\\MR\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
        elif 'the time' in query:
            start_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is {start_time}")
        
        elif 'email to mayank' in query:
            try:
                speak("what should i say")
                content = takeCommand()
                to = "mayankramani989@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                print("sorry something went wrong!")
        
        elif 'exit' in query:
            exit()
    


