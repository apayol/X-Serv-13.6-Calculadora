#!/usr/bin/python3

import sys

def sumar(a,b):
    return float(a)+float(b)
def restar(a,b):
    return float(a)-float(b)
def multiplicar(a,b):
    return float(a)*float(b)
def dividir(a,b):
    return float(a)/float(b)

if (len(sys.argv) != 4):
    sys.exit("uso: python3 calculadora.py funcion operando1 operando2")

_, funcion, op1, op2 = sys.argv 

try:
    op1 = float(op1)
    op2 = float(op2)
except ValueError:
	sys.exit("Los operandos han de ser números")

if (funcion == "sumar"):
    print("La suma resulta: " + str(sumar(op1,op2)))
elif (funcion == "restar"):
    print("La resta resulta: " + str(restar(op1,op2)))
elif (funcion == "multiplicar"):
    print("La multiplicación resulta: " + str(multiplicar(op1,op2)))
elif (funcion == "dividir"):
    try:
        print("La división resulta: " + str(dividir(op1,op2)))
    except ZeroDivisionError:
        print("División entre 0!")
else:
    print("Funciones aceptadas: sumar, restar, multiplicar o dividir")


