from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

btn1 = Button(root, text='버튼1') # tk변수, 텍스트)
btn1.pack() # 만들면 무조건 pack()을 통해 불러오기

btn2 = Button(root, padx=5, pady=10, text='버튼2') # (tk변수, padx, pady, text) 버튼 글자 기준으로 넓히기
btn2.pack()

btn3 = Button(root, padx=5, pady=10, text='버튼3') # (tk변수, padx, pady, text) 버튼 글자 기준으로 넓히기
btn3.pack()

btn4 = Button(root, width=10, height=3, text='버튼4') # (tk변수, width, height, text) 버튼 "자체"를 넓히기
btn4.pack()

btn5 = Button(root, fg='red', bg='yellow', text='버튼5') # (tk변수, fg(글자색), bg(배경색), text)
btn5.pack()

photo = PhotoImage(file='img/check.png') # 이미지 변수에 담아서 PhotoImage로 불러오기
btn6 = Button(root, image=photo) # image=에 이미지 변수 넣기
btn6.pack()

def btncmd():
    print('버튼 실행됨')

btn7 = Button(root, text='동작하는 버튼', command=btncmd) # command에 함수 이름 넣기
btn7.pack()

root.mainloop() # 계속 띄우기