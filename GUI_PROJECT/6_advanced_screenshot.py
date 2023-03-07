import time
import keyboard
from PIL import ImageGrab

def screenshot():
    current_time = time.strftime('-%Y%m%d-%H%M%S')
    img = ImageGrab.grab()
    img.save(f'img/screenshot/image{current_time}.png')

keyboard.add_hotkey('s+c', screenshot)

keyboard.wait('esc')