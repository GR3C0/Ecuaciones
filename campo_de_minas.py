# -*- coding: utf-8 -*-

""" Campo de minas """

campo = ([1,0,1], # creación del campo
		 [0,0,1],
		 [0,1,0])

#print campo[1][2] # imprime de la segunda lista el tercer numero, las listas siempre van de 0,1,2,3...
print ""
print "------------------------------------"
print "			CAMPO MINADO			"			
print "------------------------------------"
print "Hola, estás jugando al campo minado"
print "------------------------------------"
print "elige una posición para x del 0 al 2:"
eleccion_x = input(":") #pide las posiciones

def VoM(posicion):# Función vivo o muerto 
	if posicion == 1:
		print "muerto"

	else:
		print "Estas vivo, felicidades"

if eleccion_x > 2 or eleccion_x < 0:

	print "Eso no está entre el 0 y el 2"
	print "Por favor ponlo otra vez"
	eleccion_x = input(":")

	if eleccion_x <= 2 or eleccion_x >= 0:

		print "ahora tu posición para y de 0 al 2:"
		eleccion_y = input(":")

		if eleccion_y > 2 or eleccion_y < 0:
			print "Eso no está entre el 0 y el 2"
			print "Por favor ponlo otra vez"
			eleccion_y = input(":")
			posicion = campo[eleccion_x][eleccion_y] #agrupa las elecciones del usuario en una variable
			VoM(posicion)

		else:
			posicion = campo[eleccion_x][eleccion_y] #agrupa las elecciones del usuario en una variable
			VoM(posicion)	

else:		
	print "ahora tu posición para y de 0 al 2:"
	eleccion_y = input(":")

	if eleccion_y > 2 or eleccion_y < 0:
		print "Eso no está entre el 0 y el 2"
		print "Por favor ponlo otra vez"
		eleccion_y = input(":")		

	if eleccion_y <= 2 or eleccion_y >= 0:

		posicion = campo[eleccion_x][eleccion_y] #agrupa las elecciones del usuario en una variable
		VoM(posicion)
		
	else:
		posicion = campo[eleccion_x][eleccion_y] #agrupa las elecciones del usuario en una variable
		VoM(posicion)



