from PIL import ImageGrab
from time import sleep
import tkinter.messagebox as msgbox

sleep(5)

for i in range(1, 11):
    img = ImageGrab.grab()
    img.save(f"autoimg/image{i}.png")
    sleep(1)

msgbox.showinfo('알림', '스크린샷 찍기 완료')