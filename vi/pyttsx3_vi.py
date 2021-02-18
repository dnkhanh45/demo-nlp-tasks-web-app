import pyttsx3
import os
from datetime import datetime
vi_engine = pyttsx3.init()

directory = r'D:\files\vi\pyttsx3'

def pyttsx3_vi_prc(text):
    for filename in os.listdir(directory):
        os.remove(directory + '\\' + filename)

    voices = vi_engine.getProperty('voices')
    vi_engine.setProperty('voice', voices[3].id)
    vi_engine.setProperty('rate', 178)
    now = datetime.now()
    dt_string = now.strftime("%d%m%Y%H%M%S")
    filename = directory + '\\' + r'vi_pyttsx3' + str(dt_string) + r'.wav'
    vi_engine.save_to_file(text=text, filename=filename)
    vi_engine.runAndWait()

    return filename

if __name__ == '__main__':
    text = input()
    pyttsx3_vi_prc(text)
    print("xong")