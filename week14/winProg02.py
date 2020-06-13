from tkinter import *
from tkinter.filedialog import *
from tkinter import messagebox

def funQuit():
    w.quit()

def funOpen() :
    filename = askopenfilename(parent=w)
    messagebox.showinfo("선택한 파일", filename)

w = Tk()
w.geometry("400x200")

w.title("학번 이름")


mainMenu = Menu(w) #w에 해당하는 메뉴의 변수는 mainMenu
w.config(menu=mainMenu) #mainMenu를 w에 설정

fileMenu = Menu(mainMenu) #상위메뉴1
editMenu = Menu(mainMenu) #상위메뉴2
mainMenu.add_cascade(label="File", menu=fileMenu)
mainMenu.add_cascade(label="Edit", menu=editMenu)
fileMenu.add_command(label="열기", command=funOpen)
fileMenu.add_command(label="종료", command=funQuit)
editMenu.add_command(label="복사하기")
editMenu.add_command(label="잘라내기")
editMenu.add_command(label="붙여넣기")
w.mainloop()