import googletrans
from googletrans import Translator
import speech_recognition as sr
import gtts


audio_path = "./static/audio.mp3"

translator = Translator()
def dropOptions():
    lang = googletrans.LANGUAGES
    return lang

def reverseMapLang():
    lang = googletrans.LANGUAGES
    reverse = {}
    for key in lang:
        reverse[lang[key]] = key
    return reverse

def your_python_function(text, src, dest):
    if(src=="auto"):
        src = translator.detect(text).lang
    Outtext = translator.translate(text, src=src, dest=dest)
    print(Outtext.text)
    return Outtext.text

def Speech_recognize(src):
    r = sr.Recognizer()
    r.pause_threshold = 0.5
    r.energy_threshold = 2500
    with sr.Microphone() as source:
        # r.adjust_for_ambient_noise(source, duration=1)
        print("Say something")
        audio = r.listen(source, timeout=5, phrase_time_limit=6)
        print("Time over, thanks")
    try:
        print("Text: "+r.recognize_google(audio,language=src))
    except:
        pass
    return r.recognize_google(audio,language=src)

def text_to_speech(text, dest):
    tts = gtts.gTTS(text, lang=dest)
    tts.save(audio_path)
    return audio_path