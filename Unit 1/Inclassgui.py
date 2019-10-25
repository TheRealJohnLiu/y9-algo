import tkinter
import sys

def write(string):
    text_box.config(state=tkinter.NORMAL)
    text_box.insert("end", string + "\n")
    text_box.see("end")
    text_box.config(state=tkinter.DISABLED)

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

root = tkinter.Tk()

text_box = tkinter.Text(root, state=tkinter.DISABLED)
text_box.grid(row=0, column=0, columnspan=4)

button_1 = tkinter.Button(root, text="1", command=lambda: choose(1))
button_1.grid(row=1, column=0)

button_2 = tkinter.Button(root, text="2", command=lambda: choose(2))
button_2.grid(row=1, column=1)

button_3 = tkinter.Button(root, text="3", command=lambda: choose(3))
button_3.grid(row=1, column=2)

button_4 = tkinter.Button(root, text="4", command=lambda: choose(4))
button_4.grid(row=1, column=3)

root.mainloop()