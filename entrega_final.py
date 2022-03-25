from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *
import sqlite3

#-------------------------------------------------------
#FUNCTIONS
#-------------------------------------------------------

def conectar():
    con = sqlite3.connect("mibase.db")
    return con

def crear_tabla():
    con = conectar()
    cursor = con.cursor()
    sql = """CREATE TABLE jugador(
             ficha INTEGER PRIMARY KEY AUTOINCREMENT
             ,nombre varchar(100) NOT NULL
             ,apellido varchar(100) NOT NULL
             ,club varchar(100) NOT NULL
             )
    """
    cursor.execute(sql)
    con.commit()

def insertar (nombre, apellido, club, tree):
    global ficha
    tree.insert("","end",text=str(ficha+1), values=(nombre,apellido, club))
    ficha += 1
    limpiar_datos()

def borrar(tree): 
    seleccion = tree.selection()
    item = tree.item(seleccion)
    ficha=item["text"]
    """
    delete en bases
    """


    tree.delete(seleccion)
    limpiar_datos()


def click(e):
    item = tabla.focus()
    print("you clicked on", tabla.item(item,"text"))
    var_ficha.set(tabla.item(item,"text"))
    var_nombre.set(tabla.item(item,"values")[0])
    var_apellido.set(tabla.item(item,"values")[1])
    var_club.set(tabla.item(item,"values")[2])

def limpiar_datos():
    var_ficha.set("")
    var_nombre.set("")
    var_apellido.set("")
    var_club.set("")


def actualizar_treeview(tree):
    records = tree.get_children()
    for element in records:
        tree.delete(element)

    sql = "SELECT * FROM jugador ORDER BY ficha ASC"
    con=conectar()
    cursor=con.cursor()
    datos=cursor.execute(sql)

    resultado = datos.fetchall()
    for fila in resultado:
        print(fila)
        tree.insert("", 0, text=fila[0], values=(fila[1], fila[2], fila[3]))


#-------------------------------------------------------
#INICIALIZAR
#-------------------------------------------------------

try:
    conectar()
    crear_tabla()
    #actualizar_treeview(tabla)
except:
    print("Hay un error")




#-------------------------------------------------------
#VISTA
#-------------------------------------------------------

master = Tk()

#VARIABLES
var_ficha = StringVar()
var_nombre = StringVar()
var_apellido = StringVar()
var_club = StringVar()
var_filtro = StringVar()
valor_filtro = IntVar()

#LABEL TITULO
titulo = Label(master, text = "Futbolistas")
titulo.grid(sticky="ew")
titulo.grid(column=0, row=0, columnspan=8)
titulo.configure(bg= "#0000FF")

#NRO FICHA
    #LABEL
ficha_label = Label(master, text="Nro de Ficha")
ficha_label.grid(row=1, column=0)
    #ENTRY
ficha_entry = Entry(master, textvariable= var_ficha, width=25, state=DISABLED)
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

#-------------------------------------------------------
#BUTTONS
#-------------------------------------------------------

#BOTON ALTA
alta_button = Button(master, text="Alta", command=lambda:insertar(var_nombre.get(), var_apellido.get(), var_club.get(),tabla))
alta_button.grid(row=5, column=0)
#BOTON MODIFICA
modif_button = Button(master, text="Modificar")
modif_button.grid(row=5, column=1)
#BOTON BAJA
baja_button = Button(master, text="Baja", command=lambda:borrar(tabla))
baja_button.grid(row=5, column=2)
#BOTON CONSULTA
consulta_button = Button(master, text="Consulta")
consulta_button.grid(row=5, column=6)

#-------------------------------------------------------
#TREEVIEW
#-------------------------------------------------------

tabla = ttk.Treeview(master)
tabla["columns"]=("col_nombre","col_apellido","col_club")

tabla.column("#0",width=80, minwidth=80, anchor=W)
tabla.heading("#0", text="Nro Ficha")

tabla.column("col_nombre",width=240, minwidth=240, anchor=W)
tabla.heading("#1", text="Nombre")

tabla.column("col_apellido",width=240, minwidth=240, anchor=W)
tabla.heading("#2", text="Apellido")

tabla.column("col_club",width=240, minwidth=240, anchor=W)
tabla.heading("#3", text="Club")

tabla.grid(column=2, row=6, columnspan=1)

tabla.bind("<Double-1>", click)

master.mainloop()