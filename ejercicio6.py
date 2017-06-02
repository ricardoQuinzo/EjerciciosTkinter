from tkinter import *

root = Tk()

v = IntVar()
v.set(0)  # initializing the choice in 0

languages = [("ASTRONOMIA",1),("MATEMATICAS",2),("FISICA",3),("PROGRAMACION",4),("LITERATURA",5)]

def mostrar():
    print (v.get())

Label(root, text="""ESCOJA SU MATERIA FAVORITA:""",justify = LEFT,padx = 20).pack()

for txt, val in languages:
    Radiobutton(root, text=txt,indicatoron =0,width = 20,padx = 20, variable=v, command=mostrar,value=val).pack(anchor=W)

    
mainloop()
