from tkinter import *
from tkinter import ttk
from turtle import width

mi_id = 0

master = Tk() #Una sola Tk por aplicacion.

var_nombre = StringVar()
var_apeliido = StringVar()

nombre =Label (master, text= "Nombre")
nombre.grid(row=0, column=0, sticky=W)
apellido =Label (master, text= "Apeliido")
apellido.grid(row=1, column=0, sticky=W)

entry_nombre = Entry(master, textvariable=var_nombre, width=25)
entry_nombre.grid(row=0, column=1)
entry_apellido = Entry(master, textvariable=var_apeliido, width=25)
entry_apellido.grid(row=1, column=1)

def funcion_g():
    global mi_id
    mi_id += 1
    tree.insert("","end",text=str(mi_id), values=(var_nombre.get(),var_apeliido.get()))

def funcion_b():
    global mi_id
    item = tree.focus()
    print(item)
    print(tree.item(item))
    tree.delete(item)
    mi_id -= 1


tree = ttk.Treeview(master)
tree["columns"] = ("col1","col2")
tree.column("#0",width=50, minwidth=50, anchor=W)
tree.column("col1",width=80, minwidth=80, anchor=W)
tree.column("col2",width=80, minwidth=80, anchor=W)

tree.grid(column=0, row=4, columnspan=4)

boton_g = Button(master, text="Guardar", command=funcion_g)
boton_g.grid(row=2, column=1)
boton_b = Button(master, text="Borrar", command=funcion_b)
boton_b.grid(row=3, column=1)

master.mainloop()
