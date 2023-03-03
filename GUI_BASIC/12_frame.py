from tkinter import *

root = Tk()
root.title('GUI BASIC')
root.geometry('640x480+100+100')
root.resizable(False, False)
icon = PhotoImage(file = 'img/icon.png')
root.wm_iconphoto(False, icon)

Label(root, text='위 쪽에 있는 텍스트').pack(side='top')

Button(root, text='아래 쪽에 잇는 버튼').pack(side='bottom')

frame = Frame(root, relief='solid', bd=1)
frame.pack(side='left', fill='both', expand=True)

Button(frame, text='1번 버튼').pack()
Button(frame, text='2번 버튼').pack()
Button(frame, text='3번 버튼').pack()

labelframe = LabelFrame(root, text='labelframe', relief='solid')
Button(labelframe, text='4번 버튼').pack()
Button(labelframe, text='5번 버튼').pack()
labelframe.pack(side='right', fill='both', expand=True)

root.mainloop()