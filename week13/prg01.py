from tkinter import *
#import tkinter as t

w = Tk()
w.title("안녕하세요")
w.geometry("400x400")
w.resizable(width=TRUE, height=TRUE)
#이미지 처리
photo = PhotoImage(file="gif/dog.gif")
# 레이블
label1=Label(w, text="Python", font=("맑은 고딕",20), fg="blue")
txt1 = Entry(w)
label2=Label(w, text="열심히하자", anchor=SE, bg="cyan")
label3=Label(w, image=photo)

label1.pack()
txt1.pack()
label2.pack()
label3.pack()

w.mainloop()
