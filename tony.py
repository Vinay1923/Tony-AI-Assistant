import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia

engine = pyttsx3.init()


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(f"the current time is:{Time}")
    speak(Time)
    

def date():
    year = int(datetime.datetime.now().year)
    month = int(datetime.datetime.now().month)
    day = int(datetime.datetime.now().day)
    speak(f"The date is {day} {month} {year}.")
  
def wishme():
    speak("Welcome back Man!")
    hour = datetime.datetime.now().hour
    if hour >= 1 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour <= 16:
        speak("Good Afternoon!")
    elif hour >= 16 and hour <= 22:
        speak("Good Evening!")  
    else:
        speak("Good Night!")

    speak("Tony at your service, tell me how can i assist you?")    
    



def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening")
        r.pause_threshold = 1
        audio = r.listen(source)


    try:
        print("Recognizing....")
        query = r.recognize_google(audio, language = "en-in")
        print(query)
    except Exception as e:
        print(e)
        speak("Say that again please...")

        return "None"

    return query





if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()

        if 'time' in query:
            time()

        elif 'date' in query:
            date()  

        elif 'wikipedia' in query:
            speak("Searching...")
            query = query.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=1)
            print(result)
            speak(result)    

        elif 'offline' in query:
            quit()   



        
              














