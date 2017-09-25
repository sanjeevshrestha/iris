"""Iris Base Controller"""

from nltk.tokenize import word_tokenize
from tts_watson.TtsWatson import TtsWatson
import pyttsx3
import speech_recognition as sr
import configparser
import os

from iris.constants.response import CannedResponse


class IrisBaseController:
    watson_username=''
    watson_password=''
    engine = pyttsx3.init('espeak')
    engine.setProperty('rate', 150)
    recognizer = sr.Recognizer()

    def __init__(self):
        config = configparser.ConfigParser()
        config.read(['iris.cfg', os.path.expanduser('~/.iris.cfg')])
        self.watson_username = config.get('watson', 'username')
        self.watson_password = config.get('watson', 'password')

        pass

    def parse(self, argv):
        objCannedResponse = CannedResponse()
        if len(argv) == 0:
            strResp = objCannedResponse.get_default_canned_response()
            self.alison_speak(strResp)
            print(strResp)

        else:
            print(argv)
            print(word_tokenize(" ".join(argv)))
            self.alison_speak(" ".join(argv))

    def speak(self, text):
        self.engine.say(text)
        self.engine.runAndWait()
        pass

    def alison_speak(self, text):
        engine = TtsWatson(self.watson_username,self.watson_password,'en-US_AllisonVoice')
        engine.play(text)
        pass

    def listen(self):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)
        try:
            return self.recognizer.recognize_google(audio)
            # or: return recognizer.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Recog Error; {0}".format(e))

        return ""

    def respond(self, text):
        if "how are you" in text:
            self.alison_speak("I am fine!. How are you doing today?")
        else:
            self.alison_speak("Darn it!! I am still learning")

