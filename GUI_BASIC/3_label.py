from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

label1 = Label(root, text='ㅎㅇㅎㅇ') # 그냥 글자임
label1.pack()

photo = PhotoImage(file='img/check.png')
label2 = Label(root, image=photo) # 이미지 레이블에 넣기
label2.pack()

def change():
    label1.config(text='바이바이데스네')

    global photo2 # 전역으로 만들기

    # ^^^^^ 이걸 추가해줘야 함

    photo2 = PhotoImage(file='img/no.png') # 이렇게 만들면 garbage collection이라는 애가 불필요한 메모리로 인식해서
    label2.config(image=photo2) # 없애버리는데 전역 변수로 만들어야 인식을 안함

btn = Button(root, text='클릭', command=change)
btn.pack()

root.mainloop() # 계속 띄우기