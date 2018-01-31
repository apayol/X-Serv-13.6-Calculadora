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

if(len(sys.argv) != 4):
    print ("uso: python3 calculadora.py funcion operando1 operando2")
else:
    funcion = sys.argv[1]
    op1 = sys.argv[2]
    op2 = sys.argv[3]
    if (funcion == "sumar"):
        print("La suma resulta: " + str(sumar(op1,op2)))
    elif (funcion == "restar"):
        print("La resta resulta: " + str(restar(op1,op2)))
    elif (funcion == "multiplicar"):
        print("La multiplicación resulta: " + str(multiplicar(op1,op2)))
    elif (funcion == "dividir"):
        print("La división resulta: " + str(dividir(op1,op2)))
   
