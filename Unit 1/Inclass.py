from tkinter import*

def addMe():
    print(int(e1.get())-int(e2.get()))



win = Tk()
win.geometry("300x500")
win.title("simple.py")

lab1 = Label(win,text="number1")
lab2 = Label(win,text="number2")
lab1.grid(row=1,column=1)
lab2.grid(row=1,column=2)

e1=Entry(win)
e2=Entry(win)

e1.grid(row=2,column=0)
e2.grid(row=2,column=1)

b1=Button(win,text="clickme",command=addMe)

b1.grid(row=3,column=0)

mainloop()