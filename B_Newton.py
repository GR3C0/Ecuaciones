#!usr/bin/python3
#-*- coding:utf-8 -*-
#Calcular cualquier binomio mediante el teorema del binomio de Newton
import math
a = int(input('Número para a\n'))
b = int(input('Número para b\n'))
n = int(input('Número para n\n'))
def B_Newton(a,b,n):
	y = [] #Lista donde se ponen los resultados de k
	for k in range(0,n+1): #rango desde 0 hasta n (un sumatorio)
		x = math.factorial(n)/(math.factorial(k)*math.factorial(n-k))#uso de la funcion factorial para calcular
		resultado = x*a**(n-k)*b**k #calcula el resultado final
		y.append(resultado)#lo mete en la lista

	y_total = sum(y)#suma todos los resultados
	print(y_total)

B_Newton(a,b,n)
