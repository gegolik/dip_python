import string
from tkinter import *
import random

master = Tk()

#FUNCIONES
r = lambda: random.randint(0,255)

def cambiar_color():
    color="#%02X%02X%02X" % (r(),r(),r())
    master.configure(bg=color)

alta = lambda nom,ruta,desc: print (nom.get(), ruta.get(), desc.get())

#VARIABLES
var_nombre = StringVar()
var_ruta = StringVar()
var_descripcion = StringVar()

#LABEL
titulo = Label(master, text = "Ingrese sus datos")
titulo.grid(sticky="ew")
titulo.grid(column=0, row=0, columnspan=4)
titulo.configure(bg= "#FF00FF")

#NOMBRE
    #LABEL
nombre_l = Label(master, text = "Nombre")
nombre_l.grid(row=1, column=0)
    #ENTRY
nombre_e = Entry(master, textvariable= var_nombre, width=25)
nombre_e.grid(row=1,column=1)

#RUTA
    #LABEL
ruta_l = Label(master, text = "Ruta")
ruta_l.grid(row=2, column=0)
    #ENTRY
ruta_e = Entry(master, textvariable= var_ruta, width=25)
ruta_e.grid(row=2,column=1)

#DESCRIPCION
    #LABEL
descripcion_l = Label(master, text = "descripcion")
descripcion_l.grid(row=3, column=0)
    #ENTRY
descripcion_e = Entry(master, textvariable= var_descripcion, width=25)
descripcion_e.grid(row=3,column=1)

#BOTON ALTA
alta_b = Button(master, text="Alta", command= lambda: alta(var_nombre,var_ruta,var_descripcion))
alta_b.grid(row=4, column=1)

#BOTON CAMBIAR COLOR
color_b = Button(master, text="Cambio Color", command=cambiar_color)
color_b.grid(row=4, column=2)

master.mainloop()