import tkinter.ttk as ttk
from tkinter import * # 임포트
import time

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기


# progressbar = ttk.Progressbar(root, maximum=100, mode='indeterminate') # indeterminate이면 초록색이 왔다갔다 함
# progressbar.start(10) # 10ms 마다 움직임.
# progressbar.pack()

# progressbar2 = ttk.Progressbar(root, maximum=100, mode='determinate')
# progressbar2.start(10) # 10ms 마다 움직임.
# progressbar2.pack()


# def btncmd():
#     progressbar.stop()
#     progressbar2.stop() # determinate 중지하면 그냥 사라져버림

# btn = Button(root, text='중지용 버튼', command=btncmd)
# btn.pack()

p_var3 = DoubleVar()
progressbar3 = ttk.Progressbar(root, maximum=100, length=150, variable=p_var3) # double var 로 실수도 반영
progressbar3.pack()

def btncmd2():
    for i in range(1, 101):
        time.sleep(0.01)
        p_var3.set(i) # progress bar 의 값 설정
        progressbar3.update() # UI UPDATE
        print(f'현재 {p_var3.get()}%입니다')


btn = Button(root, text='시작용 버튼', command=btncmd2)
btn.pack()


root.mainloop() # 계속 띄우기