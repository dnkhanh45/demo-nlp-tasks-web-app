import pytesseract
from PIL import Image
import os

directory = r'D:\files\en\pytesseract'

def pytesseract_en_prc(imagefilename):
    image = Image.open(directory + '\\' + imagefilename)
    text = pytesseract.image_to_string(image, lang='eng')

    for filename in os.listdir(directory):
        os.remove(directory + '\\' + filename)

    return text
