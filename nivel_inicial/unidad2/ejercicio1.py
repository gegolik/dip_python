import sys

for i in range(1, len(sys.argv), 1):
    if int(sys.argv[i]) % 2 == 0:
        print ("El parametro ", i, "es par")
    else:
        print ("El parametro ", i, "NO es par")