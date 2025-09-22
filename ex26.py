from tkinter import*
from tkinter.filedialog import*

#함수 선언 부분
window = Tk()
window.geometry("400x100")

label1=Label(window, text="선택된 파일 이름")
label1.pack()

#asksaveasfile 사용자가 파일의 저장 경로와 파일명을 직접 지정하도록 할 때 사용
saveFp=asksaveasfile(parent=window,mode="w",defaultextension=".jpg",
                     filetypes=(("JPG 파일","*.jpg;*.jpeg"),("모든 파일","*.*")))

#위젯(widget)을 생성한 후에 그 속성을 변경할 때 사용하는 메서드(함수)
label1.configure(text=saveFp)
saveFp.close()

window.mainloop()