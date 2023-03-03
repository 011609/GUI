import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.geometry("300x200")  # 창의 크기를 300x200으로 설정

font_style = tkFont.Font(None, size=100)

label = tk.Label(root, text="내 라벨", font=font_style)
label.pack(fill=tk.BOTH, expand=1)  # fill과 expand 옵션을 설정하여 라벨이 창을 꽉 채우도록 함

root.mainloop()