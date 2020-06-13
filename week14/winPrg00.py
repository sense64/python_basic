from tkinter import * #tkinfer 모듈을 가지고 온다
from tkinter import messagebox #tkinfer모듈에서 messagebox함수를 가지고 옴

w = Tk() #window 생성
def messok() :
    messagebox.showinfo("메세지 확인", "안녕하세요 메제지 확인입니다")
def callback() :
    btn2["text"] = "안녕하세요 저는 홍길동입니다"
    btn2["fg"] = "white"
    btn2["bg"] = "blue"
def question() :
    result = messagebox.askquestion("선호도", "파이썬을 좋아하나요")
    if result=='yes' :
        label.configure(text="yes입니다")
    else :
        label.configure(text="no입니다")

btn1 = Button(w, text="종료", command=quit)
btn2 = Button(w, text="누르세요~~", command= callback)
btn3 = Button(w, text="메세지확인", command = messok)
btn4 = Button(w, text="파이썬선호도", command=question)
btn1.pack(side=BOTTOM,fill=X, padx=10, pady=10)
btn2.pack(side=BOTTOM,fill=X, padx=10, pady=10)
btn3.pack(side=BOTTOM,fill=X, padx=10, pady=10)
btn4.pack(side=BOTTOM,fill=X, padx=10, pady=10)
label = Label(w, text="파이썬 ?", fg="blue")
label.pack()
#btn1.place(x=100, y=10)
#btn2.place(x=100, y=70)
#btn3.place(x=100, y=130)
w.mainloop()