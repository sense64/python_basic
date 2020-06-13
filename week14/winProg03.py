from tkinter import *

w = Tk()
w.geometry("400x200")

w.title("학번 이름")

mainMenu = Menu(w)
w.config(menu=mainMenu)

fileMenu = Menu(mainMenu)
editMenu = Menu(mainMenu)
mainMenu.add_cascade(label="파일", menu=fileMenu)
fileMenu.add_command(label="파일열기", command=fun_open)
fileMenu.add_separator()
fileMenu.add_command(label="종료", command=fun_exit)
mainMenu.add_cascade(label="편집", menu=editMenu)
editMenu.add_command(label="복사")
editMenu.add_command(label="자르기")
editMenu.add_command(label="붙이기")
w.mainloop()