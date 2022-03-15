from tkinter import *
from tkinter.messagebox import *



master = Tk() #Una sola Tk por aplicacion.

def funcion_s():
    if askyesno("Titulo de la consulta de verificacion", "Contenido de la consulta de verificacion"):
        showinfo("SI", "Mensaje de informacion")
    else:
        showinfo("NO", "Esta a punto de salir")

def funcion_e(): 
    showerror("Titulo de mensaje de error", "Contenido del mensaje")
    
|

boton_e = Button(master, text="Error", command=funcion_e)
boton_e.grid(row=1, column=1)

boton_s = Button(master, text="Show", command=funcion_s)
boton_s.grid(row=2, column=1)

master.mainloop()
