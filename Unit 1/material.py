from tkinter import *
from tkinter import filedialog
from PIL import ImageTk,Image

root = Tk()
root.title("photo tagger")
root.geometry("500x350")

def test(event):
    print(event) #ensure that this line is indented

topframe = Frame(root,bg="blue",height="20")
topframe.pack(fill=X)
topframe = Frame(root,bg='blue',height='20')
topframe.pack(fill=X) # make as wide as root
can1 = Canvas(topframe,height='20',bg="blue",highlightthickness=0)
can1.create_line(0, 5, 20, 5,fill='white')
can1.create_line(0, 10, 20, 10,fill='white')
can1.create_line(0, 15, 20, 15,fill='white')
can1.bind('<Button-1>',test )
can1.pack(side=LEFT, padx=5, pady=5)     

spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)
frame = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.pack(fill=None, expand=False)
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)

spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)
frame = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
frame.pack(fill=None, expand=False)
spaceframe = Frame(root,height=10)
spaceframe.pack(fill=X)

imgframe = Frame(root,borderwidth = 1.5, relief=RAISED, width=400,height=150)
imgframe.pack(fill=None, expand=False)
canvas = Canvas(imgframe,height=150,width=200)
canvas.grid(row=0,column=0)
l1 = Label(imgframe,text="Welcome to photo tagger\nA test of Material Design in Tkinter",fg="blue")
l1.grid(row=0,column=1)
myimage = Image.open("/Users/john.liu/Desktop/CampArowhonPhotos/IMG_7719.JPG")
myimage = myimage.resize((200, 150), Image.ANTIALIAS)
myimg = ImageTk.PhotoImage(myimage)
canvas.create_image(0, 0, image=myimg, anchor = NW)

root.mainloop()