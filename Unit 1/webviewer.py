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


root = Tk()
root.title("App")
root.geometry("1000x700")
root.configure(background="#1ecbe1")
center(root)


root.mainloop()
