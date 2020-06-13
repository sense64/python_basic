from tkinter import * #tkinter 모듈로 부터 모든 함수를 가지고 온다

w = Tk() # window를 생성
w.title("안녕하세요")
w.geometry("400x200") #창의 크기
w.resizable(True,True) #창의 크기 변경여부
photo = PhotoImage(file="gif/dog.gif")
label1 = Label(w, text="199090, 홍길동", fg="blue") #Label을 생성
label2 = Label(w, image=photo)
txt1 = Entry(w)
label1.pack()
txt1.pack()
label2.pack()
w.mainloop()