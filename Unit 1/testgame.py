import tkinter as tk
import sys



def center(win):
    win.update_idletasks()
    width = win.winfo_width()
    height = win.winfo_height()

    x = (win.winfo_screenwidth() // 2) - (width // 2)
    y = (win.winfo_screenheight() // 2) - (height // 2)
    win.geometry('{}x{}+{}+{}'.format(width,height,x,y))
def write(string):
    text_box.config(state=tk.NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=tk.DISABLED)

def choose(choice):
    write("You entered door number " + str(choice) + "...")
    if choice == 1:
        write("You found a cookie!")
    elif choice == 2:
        write("You found a monster!")
    elif choice == 3:
        write("You found a...wall!")
    elif choice == 4:
        write("You found a black hole!")
    write("")


def printSomething():
   print("Hi I am trying to do something here.")

#function to print to shell.
def show_entry_fields():
    print(e1.get())
    print(e2.get())

#root is the name of the window
root = tk.Tk()
root.title("name")
root.geometry("500x500")
root.geometry('1000x600')
center(root)
root.wm_attributes("-transparent", True)
root.config(bg='systemTransparent')



tk.Label(root, text="First Name").grid(row=1)
tk.Label(root, text="Last Name").grid(row=2)

e1 = tk.Entry(root)
e2 = tk.Entry(root)

e1.grid(row=1, column=1)
e2.grid(row=2, column=1)

tkvar = tk.StringVar(root)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = tk.OptionMenu(root, tkvar, *choices)
popupMenu.grid(row = 5, column =1)

tkvar = tk.Button(root, text='Quit', command=quit).grid(row=3, column=0)
tkvar = tk.Button(root, text='Show', command=show_entry_fields).grid(row=3, column=1)

button = tk.Button(root, text="print me", command = printSomething).grid(row=4, column=1)

text_box = tk.Text(root, state=tk.DISABLED)
text_box.grid(row=0, column=0, columnspan=4)

button_1 = tk.Button(root, text="1", command=lambda: choose(1))
button_1.grid(row=7, column=0)

button_2 = tk.Button(root, text="2", command=lambda: choose(2))
button_2.grid(row=7, column=1)

button_3 = tk.Button(root, text="3", command=lambda: choose(3))
button_3.grid(row=7, column=2)

button_4 = tk.Button(root, text="4", command=lambda: choose(4))
button_4.grid(row=7, column=3)

label = tk.Label(root, text='HI THis is Label').grid(row=10, column=1)

#image = tk.PhotoImage(file='photo.gif')
#label['image'] = image
#image.grid(row=13, column=5)

#measureSystem = tk.StringVar()
#check = tk.Checkbutton(root, text='Use Metric', 
	    #command=metricChanged, variable=measureSystem,
	    #onvalue='metric', offvalue='imperial')

        
phone = tk.StringVar()
home = tk.Radiobutton(root, text='Home', variable=phone, value='home').grid(row=18, column=5)
office = tk.Radiobutton(root, text='Office', variable=phone, value='office').grid(row=18, column=6)
cell = tk.Radiobutton(root, text='Mobile', variable=phone, value='cell').grid(row=18, column=4)



root.mainloop()