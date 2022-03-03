"""A partir del ejerció 6 cree un programa con 4 funciones:
        alta() para dar de alta la nueva compra
        baja() para dar de baja una compra
        consulta() para consultar por todas las compras realizadas hasta el momento
        modificar() para modificar una compra realizada"""

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

def alta():
    cliente = input("Ingrese el nombre del cliente: ")
    total = 0
    while(True):
        cantidad = int(input("Ingrese la cantidad: "))
        p_unit = float(input ("Ingrese el precio unitario: "))
        total += cantidad * p_unit
        if not hay_productos():
            break
    
    print(f"\nEl total de {cliente} es ${total}\n\n")
    compras.append(total)

def baja():
    venta_a_bajar = int(input("Ingrese el nro de venta a bajar: "))
    if venta_a_bajar < len(compras):
        print(f"La venta {compras(venta_a_bajar)} se dio de baja")
        compras.pop(venta_a_bajar)
    else:
        print("Compra ingresada fuera de rango")

def consulta():
    pprint.pprint(compras)


def modificar():
    venta_a_modificar = int(input("Ingrese el nro de venta a modificar: "))
    if venta_a_modificar < len(compras):
        valor = float(input("Ingrese el nuevo valor de la venta: "))
        compras.pop(venta_a_modificar)
        compras.insert(venta_a_modificar, valor)
    else:
        print("Compra ingresada fuera de rango")





#Empieza el Main
inicio = True
compras = []
while(inicio):
    print("Indique la operacion a realizar: \n\t Para Alta = A \n\t Para Baja = B \n\t Para Consulta = C \n\t Para Modificar = M \n\t Para Finalizar = F")
    operacion = str(input())
    if operacion.lower() == 'a':
        alta()
    elif operacion.lower() == 'b':
      baja()
    elif operacion.lower() == 'c':
       consulta()
    elif operacion.lower() == 'm':
        modificar()
    elif operacion.lower() == 'f':
        print("FIN")
        inicio = False
    else:
        print("Opcion incorecta")