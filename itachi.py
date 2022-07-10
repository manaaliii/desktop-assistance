import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
# have chosen female voice by giving index 1
engine.setProperty('voice', voices[1].id)


# whichever we string pass here, It will speak it.
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# will greet you according to the time of the day
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if 0 <= hour < 12:
        speak("Good Morning!")
    elif 12 <= hour < 17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am uh tachi,sir , your personal assistant. How can I help you?")


# will take the input from the user and will recognise query through voice to speech
def takeCommand():
    """
    takes microphone inout from the user. and returns string output.
    """
    r = sr.Recognizer()  # help to recognize the audio
    with sr.Microphone() as source:
        print("Listening...")
        r.paude_threshold = 1  # seconds of no-audio before the end of the utterance
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print("User said: ", query)
    except Exception as e:
        # print(e)
        print("Say that again please...")
        return "None"

    return query


wishMe()
while True:
    query = takeCommand().lower()
    if 'wikipedia' in query:
        speak('Searching Wikipedia...')
        query = query.replace("wikipedia", "")
        results = wikipedia.summary(query, sentences=2)
        speak("According to Wikipedia")
        print(results)
        speak(results)

    elif 'open youtube' in query:
        webbrowser.open("youtube.com")
    elif 'open google' in query:
        webbrowser.open("google.com")
    elif 'open stackoverflow' in query:
        webbrowser.open("stackoverflow.com")

    elif 'play music' in query:
        music_dir = 'path to music directory'
        songs = os.listdir(music_dir)
        print(songs)
        ran = random.randint(0, len(songs) - 1)
        os.startfile(os.path.join(music_dir, songs[ran]))

    elif 'the time' in query:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        speak(f"sir, the time is {time}")

    elif 'open code' in query:
        codePath = "path to your IDE"
        os.startfile(codePath)

    elif 'english channel' in query:
        webbrowser.open("youtube.com\\c\\linguamarina")

    elif 'anime channel' in query:
        webbrowser.open("youtube.com\\channel\\UC05rtdBdXrK5syEvDBFGHkA")

    elif 'concert channel' in query:
        webbrowser.open("youtube.com\\user\\CapitalFMOfficial")
        
    elif 'play' in query:
        i = query.index('play')
        query = query.replace(query[:i + 6], '')
        query = query.replace(" ", "+")
        qu = 'youtube.com\\results?search_query=' + query
        webbrowser.open(qu)

    elif 'github' in query:
        webbrowser.open("github.com")

    elif 'quit' in query:
        speak("Bye sir, have a good day.")
        exit()
