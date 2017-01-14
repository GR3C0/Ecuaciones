# -*- coding: utf-8 -*-

#Calculo de matrices en python

__autor__ = "Diego Morell"

import numpy as np 

np.empty((2,3)) #Matriz vacia (el primer valor que recibe siempre es filas y el segundo columnas)

np.zeros((3,1)) #Matriz de ceros

np.ones((3,2)) #Matriz de unos

"""Funciones generales"""

a = np.zeros((2,3))

np.empty_like(a) #Matriz vacia con la forma "a" (Con el numero de columnas y filas)

np.zeros_like(a) #Matriz de zeros con forma "a"

np.ones_like(a) #Matriz de unos con forma "a"

""" Para crear una matriz identidad se puede usar np.identity """ """si las matrices no son
cuadradas np.eye """

np.identity(3) #Matriz identidad cuadrada de orden 3

np.eye(5,3) #Matriz identidad con 5 filas y 3 columnas

np.eye(4,3 k=2) #Con el parametro k podemos controlar que diagonal está llena de unos

([0,0,0],
 [1,0,0],
 [0,1,0],
 [0,0,1]	
	)

#Si se conocen los datos (insertados en un array anteriormente) se puede crear la matriz 
#con la función np.array 

np.array(
	[1,4,2] #Lista
	)
np.array( #Lista de listas
	[[2,3]
	 [1,4]]
	)

np.array(
	(0,2,3) #Tupla
	)

np.array(range(5)) #Esto daría:
	array([0,1,2,3,4])

""" Operaciones con matrices """

#Si queremos usar matrices
matriz = np.matrix([0,2,3
		  [2,4,5]
		])

#Para la traspuesta
np.transpose(matriz)

#Suma
matriz + matriz

