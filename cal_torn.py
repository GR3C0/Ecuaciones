#-*- coding: utf-8 -*-
from os import times

__version__ = 0.1

boton = False #en pruebas hasta TKinter

opciones = [ 
		"Calcular distacia",
		"Velocidad del viento",
		"Pronostico"
]
print(opciones)
opcion_usuario = input("¿Opción elegida?: ")

def calcular_distancia(): #Función que calcula la distancia con una ecuación
	while boton == True:
		print(os.times())


if opcion_usuario == "calcular distancia":
	boton = True
	calcular_distancia()
