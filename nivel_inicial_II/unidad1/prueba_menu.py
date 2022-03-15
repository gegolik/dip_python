from cProfile import label
from tkinter import *




master = Tk() #Una sola Tk por aplicacion.

def hola():
   print ("hola")


menubar = Menu(master)
menu_archivo = Menu(menubar, tearoff=0) # tearoff es la cantidad de submenues.
menu_archivo.add_command (label = "Abrir", command = hola)
menu_archivo.add_command (label = "Guardad", command = hola)
menu_archivo.add_separator()
menu_archivo.add_command (label = "Salir", command = master.quit)
menubar.add_cascade(label="Archivo", menu=menu_archivo) # A la etiqueta Archivo le asigna el menu creado


master.config(menu=menubar)
master.mainloop()
