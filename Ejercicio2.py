from tkinter import *
master = Tk()
whatever_you_do = "Tkinter es un binding de la biblioteca gráfica Tcl/Tk para el lenguaje de programación Python."
mensage = Message(master, text = whatever_you_do)
mensage.config(bg ='lightblue', font=('times', 26, 'italic'))
mensage.pack()
mainloop()
