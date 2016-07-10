#-*- coding: utf-8 -*-

autor = "__Diego__"

#script para resolver las ecuaciones de una recta

P_1 = input("Dame el primer punto: ") #asignación de valores del punto
P_2 = input("Dame el segundo punto: ")

""" Confirmación de puntos """

v_1 = input("Dame el primer dato del vector: ")
v_2 = input("Dame el segundo dato del vector: ")

""" Confirmación de vector """

punto = (P_1, P_2) 
vector = (v_1, v_2)

#Comienza a calcular todas las ecuaciones 

def Vectorial(P_1, P_2, v_1, v_2):
	print "(x,y) = (", P_1, "+", P_2, ") + (", v_1, "+", v_2, ") * t"

Vectorial(P_1, P_2, v_1, v_2)

def Parametrica(P_1, P_2, v_1, v_2):
	print "x = ", P_1 "+" 