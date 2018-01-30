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
    op1 = sys.argv[2]
    op2 = sys.argv[3]
    if (sys.argv[1] == "sumar"):
        print("La suma resulta: " + str(sumar(op1,op2)))
    elif (sys.argv[1] == "restar"):
        print("La resta resulta: " + str(restar(op1,op2)))
    elif (sys.argv[1] == "multiplicar"):
        print("La multiplicación resulta: " + str(multiplicar(op1,op2)))
    elif (sys.argv[1] == "dividir"):
        print("La división resulta: " + str(dividir(op1,op2)))
   
