from tkinter import *
master = Tk()

lbl1= Label(master, text="First name").grid(row=0)
lbl2= Label(master, text="last name").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

master.mainloop( )
