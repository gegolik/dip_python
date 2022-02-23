"""Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparecen todas las 
vocales considerando minúsculas, mayúsculas y acentos"""

import pprint

vocales = {
    "a": 0
    ,"e": 0
    ,"i": 0
    ,"o": 0
    ,"u": 0

    ,"á": 0
    ,"é": 0
    ,"í": 0
    ,"ó": 0
    ,"ú": 0

    ,"A": 0
    ,"E": 0
    ,"I": 0
    ,"O": 0
    ,"U": 0
}

oracion = input("ingrese una oracion: ")

for key in vocales:
    vocales[key] = oracion.count(key)

pprint.pprint(vocales)