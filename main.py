import functions
import pyttsx3
import speech_recognition as sr

# from gtts import gTTS#
# from audioplayer import AudioPlayer#

# Variable Implementations #
engine = pyttsx3.init()
r = sr.Recognizer()
tts = ""
while True:
    print("listening for keyword")
    with sr.Microphone() as source:
        audio = r.listen(source)
        data = r.recognize_google(audio)
        if data == "Lemon":
            break

with sr.Microphone as source:
    engine.say("This is LemonTree the Open Source virtual assistant")
    engine.runAndWait()
    print("I'm listening")
    audio = r.listen(source)
    audiodata = r.recognize_google(audio)

    # Running multiple 1 word inputs #
    if "open" or "Open" in audiodata:
        engine.say("What would you like to open")
        engine.runAndWait()
        audiodata = r.recognize_google(r.listen(source))
        functions.appOpen(audiodata)
    if "close" or "Close" in audiodata:
        engine.say("What would you like to close?")
        engine.runAndWait()
        audiodata = r.recognize_google(r.listen(source))
        functions.appClose(audiodata)
    if "search" or "Search" in audiodata:
        engine.say("what is your query")
        engine.runAndWait()
        audiodata = r.recognize_google(r.listen(source))
        functions.searchFunc(audiodata)
    if "GPT" or "gpt" in audiodata:
        engine.say("Activating ChatGPT module")
        engine.runAndWait()
        audio = r.listen(source)
        audiodata = r.recognize_google(r.listen(source))
        functions.gptModel(audiodata)
