from tkinter import *

root = Tk()

v = IntVar()
v.set(0)  # initializing the choice in 0


music = [("ROCK",1),("ROMANTICAS",2),("SALSA",3),("RAP",4),("INSTRUMENTAL",5)]

def mostrar():
    print (v.get())

    
Label(root, text="""ELIJA SU MUSICA FAVORITA:""",justify = LEFT,padx = 20).pack()

for txt, val in music:
    Radiobutton(root, text=txt,padx = 30, variable=v, command=mostrar,value=val).pack(anchor=W)

    
mainloop()
