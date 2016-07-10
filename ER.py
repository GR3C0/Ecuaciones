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
C = - v_2 + v_1 

#Comienza a calcular todas las ecuaciones 

def Vectorial(P_1, P_2, v_1, v_2):
	print " _    __          __             _       __"
	print "| |  / /__  _____/ /_____  _____(_)___ _/ /"
	print "| | / / _ \/ ___/ __/ __ \/ ___/ / __ `/ / "
	print "| |/ /  __/ /__/ /_/ /_/ / /  / / /_/ / /  "
	print "|___/\___/\___/\__/\____/_/  /_/\__,_/_/   "
	print "                                           "
	print "(x,y) = (", P_1, "+", P_2, ") + (", v_1, "+", v_2, ") * t"
	print ""

Vectorial(P_1, P_2, v_1, v_2)

def Parametrica(P_1, P_2, v_1, v_2):
	print "    ____                              __  __       _           "
	print "   / __ \____ __________ _____ ___  _/_/ / /______(_)________ _"
	print "  / /_/ / __ `/ ___/ __ `/ __ `__ \/ _ \/ __/ ___/ / ___/ __ `/"
	print " / ____/ /_/ / /  / /_/ / / / / / /  __/ /_/ /  / / /__/ /_/ / "
	print "/_/    \__,_/_/   \__,_/_/ /_/ /_/\___/\__/_/  /_/\___/\__,_/  "
	print "                                                               "
	print "x = ", P_1, "+", v_1, "*", "t"
	print "x = ", P_2, "+", v_2, "*", "t"
	print ""

Parametrica(P_1, P_2, v_1, v_2)

def Continua(P_1, P_2, v_1, v_2):
	print "   ______            __  _                  "
	print "  / ____/___  ____  / /_(_)___  __  ______ _"
	print " / /   / __ \/ __ \/ __/ / __ \/ / / / __ `/"
	print "/ /___/ /_/ / / / / /_/ / / / / /_/ / /_/ / "
	print "\____/\____/_/ /_/\__/_/_/ /_/\__,_/\__,_/  "
	print "                                            "
	print "x - ", P_1, "/", v_1, "=", "y - ",P_2, "/", v_2
	print ""

Continua(P_1, P_2, v_1, v_2)

def General(P_1, P_2, v_1, v_2):
	print "   ______                           __"
	print "  / ____/__  ____  ___  _________ _/ /"
	print " / / __/ _ \/ __ \/ _ \/ ___/ __ `/ / "
	print "/ /_/ /  __/ / / /  __/ /  / /_/ / /  "
	print "\____/\___/_/ /_/\___/_/   \__,_/_/   "
	print "                                      "
	print "Ax + By + C = 0"
	print v_2, - v_1, "+ C = 0" 
	print "C = ", -v_2 + v_1
	print ""

General(P_1, P_2, v_1, v_2)

def Explicita(P_1, P_2, v_1, v_2):
	print "    ______           ____     _ __       "
	print "   / ____/  ______  / /_/____(_) /_____ _"
	print "  / __/ | |/_/ __ \/ / / ___/ / __/ __ `/"
	print " / /____>  </ /_/ / / / /__/ / /_/ /_/ / "
	print "/_____/_/|_/ .___/_/_/\___/_/\__/\__,_/  "
	print "          /_/                            "
	print "y = mx + n"
	print "y = ", v_2/v_1 + C
	print ""

Explicita(P_1, P_2, v_1, v_2)
