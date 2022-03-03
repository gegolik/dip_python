"""A partir del ejercicio 5 cree un programa que vaya agregando en un diccionario las compras realizadas."""
#import
import pprint


#Definicion de Funciones
def iniciar_venta():
    result = input("Desea iniciar una venta? (s/n): ")
    if result.lower() == "s":
        return True
    else:
        return False

def hay_productos():
    result = input("Desea algo mas? (s/n): ")
    if result.lower() == "s":
        return True
    else:
        return False

#Empieza el Main
dictionary = {}
while(iniciar_venta()):
    cliente = str(input("Ingrese el nombre del cliente: "))
    total = 0
    while(True):
        cantidad = int(input("Ingrese la cantidad: "))
        p_unit = float(input ("Ingrese el precio unitario: "))
        total += cantidad * p_unit
        if not hay_productos():
            break

    print(f"\nEl total de {cliente} es ${total}\n\n")
    dictionary[cliente] = total


print("\nLas ventas del dia fueron por:")
pprint.pprint(dictionary)