from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기



label1 = Label(root, text='아래중에서 골라주세요').pack()



radiovar = IntVar()
btn_radio1 = Radiobutton(root, text='1번', value=1, variable=radiovar) # variable은 공유하지만 value는 따로 지정해줘야함
btn_radio1.select()
btn_radio2 = Radiobutton(root, text='2번', value=2, variable=radiovar)
btn_radio3 = Radiobutton(root, text='3번', value=3, variable=radiovar)

btn_radio1.pack()
btn_radio2.pack()
btn_radio3.pack()

label2 = Label(root, text='또 선택해주세요').pack()

btn_hehe_var = StringVar()
btn_hehe4 = Radiobutton(root, text='4번', value='4번', variable=btn_hehe_var)
btn_hehe4.select()
btn_hehe5 = Radiobutton(root, text='5번', value='5번', variable=btn_hehe_var)

btn_hehe4.pack()
btn_hehe5.pack()

def btncmd():
    print(f'라디오의 value값 : {radiovar.get()}')
    print(f'4, 5번중에는..? : {btn_hehe_var.get()}')

btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop() # 계속 띄우기