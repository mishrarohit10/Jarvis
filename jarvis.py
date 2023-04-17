import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour<=12:
        speak("Good Morning Master Wyane")
    elif hour >=12 and hour <= 18:
        speak("Good Afternoon Master Wayne")
    else:
        speak("Good Evening Master Wayne")
    speak("Master Wayne know your limits")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening.....")
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said {query}\n")

    except Exception as e:
        # print(e)
        print("Say again")
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('sendersmailaddress@gmail.com','your-password')
    server.sendmail('sendersmailaddress@gmail.com',to,content)
    server.close()


if __name__ == "__main__":
    # wishMe()
    takecommand()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query.lower():
            speak('Searching wikipedia')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open leetcode' in query:
            webbrowser.open('leetcode.com')

        # elif 'play music' in query:
        #     music_dir = diretory path
        #     songs = os.listdir(music_dir)
        #     print(songs)
        #     os.startfile(os.path.join(music_dir, songs[0]))

        elif 'the time' in query:
            str = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {str}")

        elif 'open code' in query:
            codepath = "C:\\Users\\Rohit Mishra\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak('what should i say?')
                content = takecommand()
                to = "mishrarohit316x@gmail.com"
                sendEmail(to,content)
                speak("email has been sent")
            except Exception as e:
                print(e)
                speak('im sorry master wayne')
        else:
            speak('')