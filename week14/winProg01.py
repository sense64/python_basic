from tkinter import *
from tkinter import messagebox

w = Tk()
def fun1() :
    if chk1.get()==1 :
        hobby1 = "독서"
    else :
        hobby1 = ""
    if chk2.get()==1 :
        hobby2 = "영화"
    else :
        hobby2 = ""
    messagebox.showinfo("당신의 취미", hobby1+hobby2)


def fun2() :
    if var.get() == 1 :
        label.configure(text= "파이썬")
    elif var.get() == 2 :
        label.configure(text="C++")
    else :
        label.configure(text="Java")
####
chk1 = IntVar() #변수 준비
ch1 = Checkbutton(w, text="독서", variable=chk1, command=fun1)
chk2 = IntVar() #변수 준비
ch2 = Checkbutton(w, text="영화", variable=chk2, command=fun1)

var = IntVar()#변수 준비
rb1 = Radiobutton(w, text="파이썬", variable=var, value=1, command=fun2)
rb2 = Radiobutton(w, text="C++", variable=var, value=2, command=fun2)
rb3 = Radiobutton(w, text="Java", variable=var, value=3, command=fun2)
label = Label(w, text="선택한 언어 : ", fg="red")
ch1.pack()
ch2.pack()
rb1.pack()
rb2.pack()
rb3.pack()
label.pack()
w.mainloop()