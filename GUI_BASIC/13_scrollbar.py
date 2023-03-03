from tkinter import *

root = Tk()
root.title('GUI BASIC')
root.geometry('640x480+100+100')
root.resizable(False, False)
icon = PhotoImage(file = 'img/icon.png')
root.wm_iconphoto(False, icon)

frame = Frame(root)
frame.pack()

scrollbar = Scrollbar(frame)
scrollbar.pack(side='right', fill='y')

listbox = Listbox(frame, selectmode='extended', height=10, yscrollcommand=scrollbar.set)

for i in range(1, 32):
    listbox.insert(END, str(i) + '일')
listbox.pack(side='left')

scrollbar.config(command=listbox.yview)

root.mainloop()