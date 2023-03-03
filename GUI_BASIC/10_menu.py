from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

def newfile():
    print('새 파일 만들기 버튼 클릭됨')


menu = Menu(root)

# File 메뉴
menu_file = Menu(menu, tearoff=0)
menu_file.add_command(label='New File', command=newfile) # add_command 로 추가 command=에 커맨드 추가 ㄱㄴ
menu_file.add_command(label='New Window')
menu_file.add_separator() # 분리도 ㄱㄴ
menu_file.add_command(label='Open File..')
menu_file.add_separator()
menu_file.add_command(label='Disabled menu', state='disable')
menu_file.add_separator()
menu_file.add_command(label='Exit', command=root.quit)

menu.add_cascade(label='File', menu=menu_file)

# Edit Menu
menu.add_cascade(label='Edit')

# Language 메뉴 추가 (radio 버튼을 통해서 택1)
menu_lang = Menu(menu, tearoff=0)
menu_lang.add_radiobutton(label='Python')
menu_lang.add_radiobutton(label='HTML')
menu_lang.add_radiobutton(label='CSS')

menu.add_cascade(label='Langs', menu=menu_lang)

# View 메뉴
menu_view = Menu(menu, tearoff=0)
menu_view.add_checkbutton(label='Show Minimap')
menu.add_cascade(label='View', menu=menu_view)



root.config(menu=menu)
root.mainloop() # 계속 띄우기