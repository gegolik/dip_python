#GLOBAL VARIABLES
edad_jubilatoria = 65

#FUNCTIONS STATEMENTS
def debe_jubilarse(edad):
    if edad >= edad_jubilatoria:
        print("Debe jubilarse")
    else:
        print("Puede seguir trabajando")

#MAIN
edad = int(input("Ingrese la edad: "))
debe_jubilarse(edad)