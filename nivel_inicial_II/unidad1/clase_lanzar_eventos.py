from tkinter import *
from tkinter.colorchooser import askcolor
from tkinter.filedialog import askopenfile, askopenfilename

master = Tk()

def funcion_arch():
   ruta = askopenfilename()
   print (ruta) 

def funcion_color():
   resultado = askcolor(color="#00ff00", title="El Titulo")
   print(resultado )
   print(resultado[1])

boton_a = Button(master, text="Abrir Archivo", command=funcion_arch)
boton_a.grid(row=1, column=1)

boton_c = Button(master, text="Color", command=funcion_color)
boton_c.grid(row=2, column=1)

master.mainloop()