"""Suponga que tiene una verdulería y carga la cantidad y el precio de lo comprado por un cliente. Realice un programa que tome de a uno la cantidad y el precio comprado por el cliente 
y al finalizar la compra retorne el monto total gastado. """

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

while(iniciar_venta()):
    cliente = input("Ingrese el nombre del cliente: ")
    total = 0
    while(True):
        cantidad = int(input("Ingrese la cantidad: "))
        p_unit = float(input ("Ingrese el precio unitario: "))
        total += cantidad * p_unit
        if not hay_productos():
            break
    print(f"\nEl total de {cliente} es ${total}\n\n")