from tkinter import*
from tkinter.simpledialog import *

#함수 선언 부분
window=Tk()
window.geometry("400x100")

label1=Label(window, text="입력된 값")
label1.pack()

#askinteger는 사용자에게 정수(integer) 값을 입력받기 위한 팝업창(대화상자)을 띄우는 함수
value=askinteger("확대배수","주사위 숫자(1~6)을 입력하세요", minvalue=1, maxvalue=6)

#configure(text=str(value))는 위젯(widget)에 표시되는 텍스트를 동적으로 변경할 때 사용하는 코드
label1.configure(text=str(value))
window.mainloop()