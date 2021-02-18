import pyttsx3
import os
from datetime import datetime
en_engine = pyttsx3.init()

directory = r'D:\files\en\pyttsx3'

def pyttsx3_en_prc(text):
    for filename in os.listdir(directory):
        os.remove(directory + '\\' + filename)

    voices = en_engine.getProperty('voices')
    en_engine.setProperty('voice', voices[0].id)
    en_engine.setProperty('rate', 178)
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    filename = directory + '\\' + r'en_pyttsx3' + str(dt_string) + r'.wav'
    en_engine.save_to_file(text=text, filename=filename)
    en_engine.runAndWait()

    return filename

if __name__ == '__main__':
    text = input()
    a = pyttsx3_en_prc(text)
    print(a)