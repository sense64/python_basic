from tkinter import *

def back() :
    button1["text"] = "안녕하세요"
    button1["bg"] = "blue"
    button1["fg"] = "white"
w = Tk()
w.title("안녕하세요")

# 버튼
button1 = Button(w, text="클릭하세요", command=back)
button2 = Button(w, text="종료", command=quit)
button1.pack(side=LEFT)
button2.pack(side=LEFT)

w.mainloop()
