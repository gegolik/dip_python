import sys

for i in range(1, len(sys.argv)):
    if (sys.argv[i] % 2) == 0:
        print("El primer parametro es multiplo de 2 ");
    else:
        print("el segudo parametro no es multiplo de 2");
