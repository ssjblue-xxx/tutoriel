from tkinter import *

test = Tk()

def yes():
    print('le texte que vous voulez')

b = Button(test, text="appuie ici", command=yes)
b.pack()

test.mainloop()
