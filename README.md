# **GUI BASIC**

### **영상** [**링크**](https://www.youtube.com/watch?v=bKPIcoou9N8, "ㅅㄹㅎㄴㄷ!")

# **Basic**

```py
from tkinter import *

root = Tk()
root.title('GUI BASIC')
root.geometry('640x480+100+100')
root.resizable(False, False)
icon = PhotoImage(file = 'img/icon.png')
root.wm_iconphoto(False, icon)

root.mainloop()
```

# **With Button**

```py
from tkinter import * # 임포트

root = Tk() # 변수 설정
root.title('GUI BASIC') # 창 이름
root.geometry('640x480+50+50') # 가로 * 세로 + X좌표 + Y좌표
root.resizable(False, False) # X, Y 창 값 변경 불가
icon = PhotoImage(file = 'img/icon.png') # icon 변수 안에 이미지 넣어주기
root.iconphoto(False, icon) # False(필수) 넣고 이미지 변수 넣기

def btncmd():
    pass

btn = Button(root, text='버튼', command=btncmd)
btn.pack()

root.mainloop() # 계속 띄우기
```


# **Progress**

|제목|완료 / 날짜|
|:------:|:---:|
|**1. 기본 프레임**|✅ 2023/02/11|
|**2. 버튼**|✅ 2023/02/11|
|**3. 레이블**|✅ 2023/02/11|
|**4. 텍스트 & 엔트리**|✅ 2023/02/11|
|**5. 리스트 박스**|✅ 2023/02/11|
|**6. 체크 버튼**|✅ 2023/02/11|
|**7. 라디오 버튼**|✅ 2023/02/11|
|**8. 콤보 박스**|✅ 2023/02/11|
|**9. 프로그레스 바**|✅ 2023/03/03|
|**10. 메뉴**|✅ 2023/03/03|
|**11. 메시지 박스**|✅ 2023/03/03|
|**12. 프레임**|✅ 2023/03/03|
|**13. 스크롤 바**|✅ 2023/03/03|
|**14. 그리드**|✅ 2023/03/04|
|**15. 퀴즈 (메모장 만들기)**|✅ 2023/03/05|
|**16. 프로젝트**|✅ 2023/03/06~07|
|**17. 스크린샷 프로그램**|✅ 2023/03/07|