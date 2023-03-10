import tkinter.ttk as ttk
import tkinter.messagebox as msgbox
from tkinter import * # 임포트
from tkinter import filedialog
from PIL import Image
import os

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title='이미지 파일을 선택해주세요.', \
            filetypes=(('PNG 파일', "*.png"), ('모든 파일', "*.*"),), \
            initialdir=r'C:\Users\rub77\OneDrive\Desktop\codespace\GUI(PRIVATE)\img')
    
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 선택 삭제
def delete_file():
    # print(list_file.curselection())

    for index in reversed(list_file.curselection()):
        list_file.delete(index)

# 저장 경로 (폴더)
def browse_dest_path():
    folder_selected = filedialog.askdirectory()
    if folder_selected == '':
        return
    
    # print(folder_selected)
    txt_dest_path.delete(0, END)
    txt_dest_path.insert(0, folder_selected)    

# 이미지 통합 
def merge_image():
    # print(f'가로 넓이 : {cmb_width.get()}')
    # print(f'간격 : {cmb_space.get()}')
    # print(f'포맷 : {cmb_format.get()}')

    try:
    # 가로 넓이
        img_width = cmb_width.get()
        if img_width == '원본 유지':
            img_width = -1
        
        else:
            img_width = int(img_width)

        # 간격
        img_space = cmb_space.get()

        if img_space == '좁게':
            img_space = 10
        elif img_space == '보통':
            img_space = 25
        elif img_space == '넓게':
            img_space = 40
        else: # 없음
            img_space = 0

        # 포맷
        img_format = cmb_format.get().lower() # PNG JPG BMP 소문자로 변경
        print(img_format)

        ##############################################################

        images = [Image.open(x) for x in list_file.get(0, END)]
        
        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []
        if img_width > -1:
            # width 값 변경
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            pass # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]

        # 계산식
        # 100 * 60 이미지가 있음 -> width 를 80으로 줄이면 height는??
        # (원본 width) : (원본 height) = (변경 width) : (변경 height)
        # 100 : 60 = 80 : ???
        # x : y = x' : y'
        # xy' = x'y
        # y' = x'y / x -> 이 식을 적용함
        # 100 : 60 = 80:48

        # 코드에 대입하려면..
        # x = width = size[0]
        # y = height = size[1]
        # x' = img_width
        # y' = x'y / x = img_width * size[1] / size[0]




        widths, heights = zip(*(image_sizes))

        # 최대 넓이 전체 높이 구해오기
        max_width = max(widths)
        total_height = sum(heights)

        # 스케치북 준비
        if img_space > 0: # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) -1))
        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255)) # 배경 흰색
        y_offset = 0 # y 위치

        for idx, img in enumerate(images):
            # width 가 원본유지가 아니면 이미지 크기를 조정해야함.
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space) # height 값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100 # 실제 percent 정보를 계산
            p_var.set(progress)
            progress_bar.update()

        # 포맷 옵션 처리
        file_name = 'result_image.' + img_format
        dest_path = os.path.join(txt_dest_path.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo('알림', '작업 완료!')
    
    except PermissionError:
        msgbox.showerror('ERROR', '파일에 접근이 불가합니다 C:/ 드라이브나 다른 접근이 불가한 위치에서는 프로그램을 작동시킬수 없습니다. \n\n저장 경로를 바꿔주세요.')

    except FileNotFoundError:
        msgbox.showerror('ERROR', '파일을 찾을 수 없습니다. \n\n저장 경로를 바꿔주세요.')
        
    except Exception as err:
        msgbox.showerror('ERROR', err)

# 시작
def start():
    # 각 옵션들 값을 확인
    # print(f'가로 넓이 : {cmb_width.get()}')
    # print(f'간격 : {cmb_space.get()}')
    # print(f'포맷 : {cmb_format.get()}')

    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning('경고', '이미지 파일을 추가해주세요')
        return
    
    # 저장 경로 확인
    if len(txt_dest_path.get()) == 0:
        msgbox.showwarning('경고', '저장 경로를 선택하세요')
        return
    
    # 이미지 통합 작업
    merge_image()



# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill='x', padx=5, pady=5)

btn_add_file = Button(file_frame, text='파일 추가', padx=5, pady=5, width=12, relief='groove', command=add_file)
btn_add_file.pack(side='left')

btn_del_file = Button(file_frame, text='선택 삭제', padx=5, pady=5, width=12, relief='groove', command=delete_file)
btn_del_file.pack(side='right')

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill='both', padx=5, pady=5)

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side='right', fill='y')

list_file = Listbox(list_frame, selectmode='extended', height=15, yscrollcommand=scrollbar.set)
list_file.pack(side='left', fill='both', expand=True)

scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
path_frame = LabelFrame(root, text='저장 경로')
path_frame.pack(fill='x', padx=5, pady=5, ipady=5)

txt_dest_path = Entry(path_frame)
txt_dest_path.pack(side='left', fill='x', expand=True, padx=5, pady=5, ipady=4) # 높이 변경

btn_dest_path = Button(path_frame, text='찾아보기', width=10, relief='groove', command=browse_dest_path)
btn_dest_path.pack(side='right', padx=5, pady=5)

# 옵션 프레임
frame_option = LabelFrame(root, text='옵션')
frame_option.pack(padx=5, pady=5, ipady=5)

# 1. 가로 넓이 옵션
# 1-2. 가로 넓이 레이블
lbl_width = Label(frame_option, text='가로 넓이', width=8)
lbl_width.pack(side='left', padx=5, pady=5)

# 2-3. 가로 넓이 콤보박스
option_width = ['원본 유지', '1024', '800', '640']
cmb_width = ttk.Combobox(frame_option, state='readonly', values=option_width, width=10)
cmb_width.current(0)
cmb_width.pack(side='left', padx=5, pady=5)


# 2. 간격 옵션
# 2-2. 간격 옵션 레이블

lbl_space = Label(frame_option, text='간격', width=8)
lbl_space.pack(side='left', padx=5, pady=5)

# 2-3. 가로 넓이 콤보박스
option_space = ['없음', '좁게', '보통', '넓게']
cmb_space = ttk.Combobox(frame_option, state='readonly', values=option_space, width=10)
cmb_space.current(0)
cmb_space.pack(side='left', padx=5, pady=5)

# 3. 파일 포맷 옵션
# 3-2. 파일 포맷 옵션 레이블

lbl_format = Label(frame_option, text='포맷', width=8)
lbl_format.pack(side='left', padx=5, pady=5)

# 3-3. 파일 포맷 옵션 콤보박스
option_format = ['PNG', 'JPG', 'BMP']
cmb_format = ttk.Combobox(frame_option, state='readonly', values=option_format, width=10)
cmb_format.current(0)
cmb_format.pack(side='left', padx=5, pady=5)

# 진행 상황 프로그래스 바
frame_progress = LabelFrame(root, text='진행 상황')
frame_progress.pack(fill='x', padx=5, pady=5, ipady=5)

p_var = DoubleVar()
progress_bar = ttk.Progressbar(frame_progress, maximum=100, variable=p_var)
progress_bar.pack(fill='x', padx=10, pady=10)

# 실행 프레임
frame_run = Frame(root)
frame_run.pack(fill='x', padx=5, pady=5)

btn_close = Button(frame_run, padx=5, pady=5, text='종료', width=12, command=root.quit)
btn_close.pack(side='right', padx=5, pady=5)

btn_start = Button(frame_run, padx=5, pady=5, text='시작!', width=12, command=start)
btn_start.pack(side='right', padx=5, pady=5)


root.mainloop() # 계속 띄우기