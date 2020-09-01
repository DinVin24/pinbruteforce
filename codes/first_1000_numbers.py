try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import pyscreenshot as ImageGrab
pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'
door = "THIS DOOR IS LOCKED"
import pyautogui
a = 0
b = 0
c = 0
d = 0
while a < 1:
        if d == 10:
            d=0
            c+=1

        if c==10:
            c=0
            b+=1

        if b==10:
            b=0
            a+=1
        pyautogui.press("e")
        im = ImageGrab.grab(bbox=(750, 377, 1170, 417))  # This is locked
        im.save('door_locked.png')  # saving the shit
        name = pytesseract.image_to_string(Image.open('door_locked.png'))
        if(door != name):
            break
        pyautogui.click(959, 538) #write
        pyautogui.write('%a%a%a%a\n' %(a,b,c,d))
        pyautogui.click(960, 616) #ACCEPT
        print('%a%a%a%a' %(a,b,c,d))
        d+=1