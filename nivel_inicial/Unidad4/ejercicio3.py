"""Crear una función lambda que sea equivalente a la siguiente función:
def sumar(valor1, valor2):
        res = valor1 + valor2
        return res
"""

def sumar(valor1, valor2):
        res = valor1 + valor2
        return res

sumar_lambda = lambda v1,v2: v1+v2


print(sumar(1,158))
print(sumar_lambda(1,158))