from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기



listbox = Listbox(root, selectmode='extended', height=0) # selectmode="extended" 또는 "single"로 설정 ㄱㄴ
listbox.insert(0, '1번')
listbox.insert(1, '2번')
listbox.insert(2, '3번')
listbox.insert(END, '4번')
listbox.insert(END, '5번') # END로 하면 맨 마지막에 넣어짐
listbox.pack()

def btncmd():
    # 삭제
    # listbox.delete(END) # 맨 뒤 항목 삭제

    # 갯수 확인
    # print(f'리스트에는 {listbox.size()}개가 있어요')

    # 항목 확인 (시작 인덱스, 끝 인덱스)
    # print(f'1번째부터 3번쨰까지의 항목 : {listbox.get(0, 2)}')

    # 선택된 항목 확인
    print(f'선택된 항목 : {listbox.curselection()}')


btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop() # 계속 띄우기