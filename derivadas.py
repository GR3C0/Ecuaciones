#!/usr/bin/env python
# -*- coding: utf-8 -*-
# tipo_derivada = tp 
from math import sqrt

print "¿Que derivada quieres? (funcion lineal, potencia, raiz cuadrada)"
tp = raw_input(":") 

def funcion_lineal(a,b,c):
	""" derivada de una funcion lineal """
	print ""
	print "f(x) =",a,b

def potencia(a,n):
	""" derivada de una potencia, args la potencia y el número """
	print ""
	print "f(x) =",a,"**",n	
	print ""
	print "Ahora tu derivada"
	print n * a**(n - 1) * a
	print ""
	print "Y la formula"
	print "f'(x) = n * a**(n - 1) * a"
	print ""

def raiz_cuadrada(u):
	""" derivada de una raiz cuadrada, args la raiz"""	
	print ""
	print "f(x) = √", u
	print ""
	print "Ahora tu derivada"
	print u/2*sqrt(u)
	print ""
	print "Y la formula"
	print "f'(x) = u / 2 * √2" 
	print ""

#elección de tipo de formula
if tp == "funcion lineal": #cada condicional tiene una función y sus argumentos correspodientes
	print "Dame los números"
	print "a"
	a = input(":")
	print "b"
	b = input(":")
	funcion_lineal()

elif tp == "potencia":
	print "Dame la base"
	a = input(":")
	print "Ahora el exponente"
	n = input(":")
	potencia(a,n)

elif tp == "raiz cuadrada":
	print "Dame la raiz"
	u = input(":")
	raiz_cuadrada(u)

else:
	print "¿Que quieres tio?"		