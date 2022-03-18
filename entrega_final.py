from tkinter import *
from tkinter.tix import COLUMN

master = Tk()
#VARIABLES
var_ficha = StringVar()
var_nombre = StringVar()
var_apellido = StringVar()
var_club = StringVar()
var_filtro = StringVar()
valor_filtro = IntVar()


#LABEL
titulo = Label(master, text = "Futbolistas")
titulo.grid(sticky="ew")
titulo.grid(column=0, row=0, columnspan=8)
titulo.configure(bg= "#0000FF")


#NRO FICHA
    #LABEL
ficha_label = Label(master, text="Nro de Ficha")
ficha_label.grid(row=1, column=0)
    #ENTRY
ficha_entry = Entry(master, textvariable= var_ficha, width=25)
ficha_entry.grid(row=1,column=2)

#NOMBRE
    #LABEL
nombre_label = Label(master, text="Nombre")
nombre_label.grid(row=2, column=0)
    #ENTRY
nombre_entry = Entry(master, textvariable= var_nombre, width=25)
nombre_entry.grid(row=2,column=2)


#APELLIDO
    #LABEL
apellido_label = Label(master, text="Apellido")
apellido_label.grid(row=3, column=0)
    #ENTRY
apellido_entry = Entry(master, textvariable=var_apellido, width=25)
apellido_entry.grid(row=3, column=2)

#CLUB
    #LABEL
club_label = Label(master, text="Club")
club_label.grid(row=4, column=0)
    #ENTRY
club_entry = Entry(master, textvariable=var_club, width= 25)
club_entry.grid(row=4, column=2)

#CONSULTA
#LABEL
consulta_label = Label(master, text="Consulta")
consulta_label.grid(row=1, column=6)

#RADIO BUTTONS

ficha_radio = Radiobutton(master, text='Por Nro Ficha', variable=valor_filtro, value=1)
ficha_radio.grid(row=2,column=6)

apellido_radio = Radiobutton(master, text='Por Apellido',variable=valor_filtro, value=2) 
apellido_radio.grid(row=2,column=7)

    #ENTRY FILTRO
filtro_entry = Entry(master, textvariable= var_filtro, width=25)
filtro_entry.grid(row=3,column=6)


#BOTON ALTA
alta_button = Button(master, text="Alta")
alta_button.grid(row=5, column=0)

#BOTON MODIFICA
modif_button = Button(master, text="Modificar")
modif_button.grid(row=5, column=1)

#BOTON BAJA
baja_button = Button(master, text="Baja")
baja_button.grid(row=5, column=2)


#BOTON CONSULTA
consulta_button = Button(master, text="Consulta")
consulta_button.grid(row=5, column=6)

master.mainloop()