from final.vi import pyttsx3_vi
from final.en import pyttsx3_en
if __name__ == '__main__':
    pyttsx3_vi.vi_engine.say("Chào bạn")
    pyttsx3_vi.vi_engine.runAndWait()

    pyttsx3_en.en_engine.say("Hello")
    pyttsx3_en.en_engine.runAndWait()