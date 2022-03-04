"""Crear una función lambda que sea equivalente a la siguiente función:
def multiplicar_por_tres(valor):
        res = 3 * valor
        return res
"""

def multiplicar_por_tres(valor):
        res = 3 * valor
        return res

mult_por_tres = lambda nro: nro * 3


print(multiplicar_por_tres(4))
print(mult_por_tres(4))