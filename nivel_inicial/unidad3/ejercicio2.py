""""Escriba un programa que consulte al usuario por una oración y comente al usuario cuantas veces aparece la letra “a”. """

oracion = input("Ingrese una oracion: ")
char = input("Ingrese el caracter a buscar: ")
print(f"La cantidad de veces que aparece '{char}' es : {oracion.count(char)}")