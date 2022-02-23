def crear_lista(x,y):
    list=[x,y,x + y]
    return list

valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))


print ("La lista tiene los valores: ", crear_lista(valor1,valor2))