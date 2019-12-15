from tkinter import *
import os
from tkinter import messagebox
root = Tk()
root.iconbitmap("LOL.ico")

root.title("Dash")
root.geometry("500x500")

#lbl.pack()
def ext():
    quit()

entr = Text(width=500, height=50)

#def func():
    #messagebox.showinfo("TEST MSGBOX", entr.window_create(INSERT, window=messagebox))
    #entr.window_create(INSERT, window=lbl)


def runp():
    os.system("python prog.py")

btn = Button(text="<< Run program >>", width=500, height=2, command=runp)

def newf():
    entr.pack()
    #scroll = Scrollbar(command=entr.yview)
    #scroll.pack(side=LEFT, fill=Y)
    btn.pack()
    #entr.config(yscrollcommand=scroll.set)

def savef():
    svf = open("prog.py", "w")
    s = entr.get(1.0, END)
    svf.write(s)

def inf():
    messagebox.showinfo("About IDLE", "Version: v1.0\nLicense: GPL3\nEmail: titan1234eti@gmail.com")


flmn = Menu()
flmn.add_command(label="New", command=newf)
flmn.add_command(label="Open")
flmn.add_command(label="Save", command=savef)
flmn.add_separator()
flmn.add_command(label="Exit", command=ext)

menum = Menu()
menum.add_cascade(label="File", menu=flmn)
menum.add_cascade(label="Info", command=inf)

root.config(menu=menum, bg="#000000")


root.mainloop()
