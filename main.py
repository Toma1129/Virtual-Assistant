import speech_recognition as sr
import pyttsx3
import datetime
import pywhatkit
import wikipedia
import pyjokes

listener = sr.Recognizer()
pluto = pyttsx3.init()

# if you want to change voice [voices = alexa.getProperty('voices')
# alexa.setProperty('voice', voices[1].id)]

def talk(text):
    pluto.say(text)
    pluto.runAndWait()


def take_command():
    try:
        with sr.Microphone() as source:
            print('Device is listening, please speak...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'pluto' in command:
                command = command.replace('pluto', '')
    except:
        pass
    return command


def run_pluto():
    command = take_command()

    if 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        print('Current time is ' + time)
        talk('Current time is ' + time)
    elif 'play' in command:
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)
    elif 'tell me about' in command:
        wiki = command.replace('tell me about', '')
        info = wikipedia.summary(wiki, 2)
        print(info)
        talk(info)
    elif 'how are you' in command:
        talk('Alhamdulillah, I am well')
    elif 'are you single' in command:
        talk('I am in a relationship with wifi')
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk('Sorry I didnot get your question, I can search it from google')
        pywhatkit.search(command)


while True:
    run_pluto()