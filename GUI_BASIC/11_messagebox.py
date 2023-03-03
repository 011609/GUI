import tkinter.messagebox as msgbox
from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

def info():
    msgbox.showinfo('알림', '엄청나진 않지만 대단한 알림의 내용')

def warn():
    msgbox.showwarning('경고', '엄청나진 않지만 대단한 경고의 내용')

def error():
    msgbox.showerror('에러', '엄청나진 않지만 대단한 에러의 내용')

def okcancel():
    msgbox.askokcancel('확인 / 취소', '엄청나진 않지만 대단한 확인 / 취소의 내용')

def retrycancel():
    response = msgbox.askretrycancel('재시도 / 취소', '엄청나진 않지만 대단한 재시도의 내용')
    print(f'응답은 {response}')
    if response == True:
        print('계속 함')

    if response == False:
        print('종료!')
        root.quit()

def yesno():
    msgbox.askyesno('예? / 아니요?', '엄청나진 않지만 대단한 예? / 아니요? 의 내용')

def yesnocancel():
    response = msgbox.askyesnocancel(title=None, message='예? 아니요? 취소!')
    print(f'응답은 {response}')
    if response == True:
        print('계속 함')

    if response == False:
        print('종료!')
        root.quit()

    if response == None:
        print('취소됨')

btn = Button(root, text='INFO', command=info).pack()
btn = Button(root, text='WARNING', command=warn).pack()
btn = Button(root, text='ERROR', command=error).pack()
btn = Button(root, text='확인 또는 취소', command=okcancel).pack()
btn = Button(root, text='재시도', command=retrycancel).pack()
btn = Button(root, text='예? 아니요?', command=yesno).pack()
btn = Button(root, text='예? 아니요? 취소!', command=yesnocancel).pack()

root.mainloop() # 계속 띄우기