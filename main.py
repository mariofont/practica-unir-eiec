
#!/usr/bin/python

import getopt
import sys

# Feature de Julen, aceptar argumento por linea de comando
def main(argv):
    order = ''
    try:
        opts, args = getopt.getopt(argv, "hi:o:", ["ifile=", "ofile="])
    except getopt.GetoptError:
        print('main.py -o a')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print('main.py -o a')
            sys.exit()
        elif opt in ("-o", "--order"):
            order = arg
    print('El orden es', "ascendente" if order == "a" else "descendente")


if __name__ == "__main__":
    print("¡Hola, mundo! Esto es una prueba del primer commit.")
    main(sys.argv[1:])
