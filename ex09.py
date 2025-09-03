from tkinter import*
window = Tk()

def myFunc() :
    if var.get() == 1 :
        lable1.configure(text = "파이썬")
    elif var.get() == 2 :
        lable1.configure(text = "c++")
    else :
        lable1.configure(text = "Java")

var = IntVar()
rb1=Radiobutton(window, text="파이썬", variable=var, value=1, command=myFunc)
rb2=Radiobutton(window, text="c++", variable=var, value=2, command=myFunc)
rb3=Radiobutton(window, text="Java", variable=var, value=3, command=myFunc)

lable1=Label(window, text="선택한 언어 : ", fg="red")

rb1.pack()
rb2.pack()
rb3.pack()
lable1.pack()

window.mainloop()