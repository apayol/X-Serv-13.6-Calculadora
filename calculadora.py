#!/usr/bin/python3
# ADRIÁN PAYOL MONTERO
import sys

if len(sys.argv) != 4:    # han de ser 4 argumentos
    sys.exit("uso: python3 calculadora.py función operando1 operando2")

_, funcion, op1, op2 = sys.argv    # guardo los argumentos

try:
    op1 = float(op1)
    op2 = float(op2)
except ValueError:
    sys.exit("Los operandos han de ser números")

if funcion == "sumar":
    print("La suma resulta: " + str(op1 + op2))
elif funcion == "restar":
    print("La resta resulta: " + str(op1 - op2))
elif funcion == "multiplicar":
    print("La multiplicación resulta: " + str(op1 * op2))
elif funcion == "dividir":
    try:
        print("La división resulta: " + str(op1 / op2))
    except ZeroDivisionError:
        sys.exit("Indefinido, división entre 0!")
else:
    print("Funciones aceptadas: sumar, restar, multiplicar o dividir")
