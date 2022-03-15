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


menu_edicion = Menu(menubar, tearoff=0) # tearoff es la cantidad de submenues.
menu_edicion.add_command (label = "Abrir", command = hola)
menu_edicion.add_command (label = "Guardad", command = hola)
menu_edicion.add_separator()
menu_edicion.add_command (label = "Salir", command = master.quit)
menubar.add_cascade(label="Editar", menu=menu_edicion) # A la etiqueta Archivo le asigna el menu creado


submenu = Menu(menu_edicion, tearoff=True)
submenu.add_command (label = "Editar Color", command = hola)
submenu.add_command (label = "Rotar Imagen", command = hola)
menu_edicion.add_cascade(label="Otros", menu=submenu)


master.config(menu=menubar)
master.mainloop()
