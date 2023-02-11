from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기


txt = Text(root, width=30, height=5) # 텍스트는 여러줄 입력받기
txt.pack()

txt.insert(END, "글자 미리 입력하기") # insert를 통해서 글자를 미리 입력할수 있음

entry = Entry(root, width=30) # 엔트리는 한 줄 입력받기
entry.pack()

entry.insert(0, '글자 미리 넣기')

def btncmd():
    print(txt.get("1.0", END)) # 처음부터 끝까지 텍스트를 다 가져오기
    print(entry.get()) # 엔트리는 간편하게 get()만 사용해주면 됨

    txt.delete("1.0", END)
    entry.delete(0, END) # delete로 지우기

btn = Button(root, text='클릭', command=btncmd)
btn.pack()


root.mainloop() # 계속 띄우기