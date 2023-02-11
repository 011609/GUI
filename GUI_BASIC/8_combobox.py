from tkinter import * # 임포트
import tkinter.ttk as ttk

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기



values = [str(i) + "일" for i in range(1, 32)]
combobox = ttk.Combobox(root, height=5, values=values)
combobox.pack()
combobox.set('아래 일중에서 선택해주십쇼')

readonly = ttk.Combobox(root, height=10, values=values, state='readonly')
readonly.current(0) # 0번쨰(1번째) 값 자동 선택
readonly.pack()

def btncmd():
    print(combobox.get()) # 선택 값 표시
    print(readonly.get()) # 선택 값 표시

btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop() # 계속 띄우기