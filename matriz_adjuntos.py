#!usr/bin/python3
# -*- coding: utf-8 -*-
import numpy as np

# Pide filas y columnas
filas = int(input("Número de filas:\n"))
columnas = int(input("Número de columnas:\n"))

lista_numeros = []  # Lista de todos los números de la matriz

for i in range(filas * columnas):  # ciclo para pedir todos los números
	print("Número: ", i + 1)
	x = int(input(":"))
	lista_numeros.append(x)  # Insterta en la lista todos los números

print(np.array(lista_numeros).reshape(filas, columnas))  # Utiliza la función 'array' de numpy
# y para utilizar el número exacto de filas y columnas, la función 'reshape'

def determinante(lista_numeros):  # Función que contiene la fórmula
	adj = [] # Lista donde van los números que quedan después de eliminar n-1
	if len(lista_numeros) >= 4: #or len(adj) <= 2:
		for i in lista_numeros:
			lista_numeros.remove(i)


		print(lista_numeros)
		# print(lista_numeros[3] - 1)

while 1:  # Siempre se inicia la función
	determinante(lista_numeros)
	break
