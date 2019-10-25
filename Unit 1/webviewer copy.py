from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()
    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def test(event):
    print(event) #ensure that this line is indented

root = Tk()
root.title("app")
root.geometry("1000x700")
root.configure(background="#1ecbe1")
center(root)


topframe = Frame(root,bg="blue",height="20")
topframe.pack(fill=X)
topframe = Frame(root,bg='blue',height='20')
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='yellow')
can1.create_line(0, 10, 20, 10,fill='yellow')
can1.create_line(0, 15, 20, 15,fill='yellow')
can1.bind('<Button-1>',test )
can1.pack(side=LEFT, padx=5, pady=5)     

spaceframe = Frame(root,height=10)
spaceframe.pack(fill=Y)
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=Y)
frame = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.pack(fill=None, expand=False)

spaceframe = Frame(root,height=10)
spaceframe.pack(fill=Y)
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=Y)
frame = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.pack(fill=None, expand=False)







root.mainloop()