try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract

import pyscreenshot as ImageGrab
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'

door = "THIS DOOR IS LOCKED"

import pyautogui
a = 1000
while a <= 9999:
        pyautogui.press("e")
        im = ImageGrab.grab(bbox=(750, 377, 1170, 417))  # This is locked
        im.save('door_locked.png')  # saving the shit
        name = pytesseract.image_to_string(Image.open('door_locked.png'))
        if(door != name):
            break
        pyautogui.click(959, 538) #write
        pyautogui.write('%a' %(a))
        pyautogui.click(960, 616) #ACCEPT
        print('%a\n' %(a))
        a+=1