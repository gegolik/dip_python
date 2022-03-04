""" Cree una función que tome la siguiente lista y reordene de menor a mayor sus componentes:
[3, 44, 21, 78, 5, 56, 9]

"""

def ordenar(list):
    hubo_cambios = True
    while hubo_cambios:
        hubo_cambios = False
        for i in range (len(lista)-1):
            if list[i] > list[i+1]:
                aux = list[i+1]
                list[i+1] = list[i]
                list[i] = aux
                hubo_cambios = True
            


lista = [3, 44, 21, 78, 5, 56, 9]
ordenar(lista)
print(lista)

"""Como pasar paratros por direccion para que puedan ser modificados en una funcion?"""
