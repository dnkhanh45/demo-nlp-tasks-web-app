import speech_recognition as sr
import os

r = sr.Recognizer()
directory = r'D:\files\vi\speech_recognition'
def speech_recognition_vi_prc(wavfilename):
    with sr.WavFile(directory + '\\' + wavfilename) as source:
        audio = r.record(source)
    try:
        text = r.recognize_google(audio, language='vi-VN')  # 'en-US'
    except sr.UnknownValueError:
        text = "Google Speech Recognition could not understand audio"
    except sr.RequestError:
        text = "Could not request results from Google SpeechRecognition service"

    for filename in os.listdir(directory):
        os.remove(directory + '\\' + filename)

    return text
