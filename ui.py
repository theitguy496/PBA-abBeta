from tkinter import *
import URLCHKR



root= Tk()

e = Entry(root, width=50)

e.pack()

def myClick():
    from URLCHKR import url_check
    label = Label(root, url_check)
    label.pack()
    label.config(url=entry.get(url_check())


button = Button(root,text="Run", command=myClick)
button.pack()

root.mainloop()

