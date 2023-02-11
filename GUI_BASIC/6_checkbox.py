from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

chkvar = IntVar() # chkvar 에 int 형으로 값을 저장한다
chkbox = Checkbutton(root, text='체크 박스', variable=chkvar)
chkbox.pack()
chkbox.select() # deselect를 하면 선택이 안됨


chkvar2 = IntVar()
chkbox2 = Checkbutton(root, text='2번째 체크 박스', variable=chkvar2)
chkbox2.pack()



def btncmd():
    print(f'체크박스의 상태는 : {chkvar.get()}') # 0 : 체크 해제, 1 : 체크 됨
    print(f'체크박스2의 상태는 : {chkvar2.get()}') # 0 : 체크 해제, 1 : 체크 됨

btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop() # 계속 띄우기