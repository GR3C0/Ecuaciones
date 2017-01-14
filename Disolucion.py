#!usr/bin/python3
#-*- coding:utf-8 -*-
#Script para calcular disoluciones Ácido-Base
#Elementos = {'C': 12, #Diccionario de elementos con sus números moleculares
#			 'O': 16,
#			 'N': 14,
#			 'H': 1,
#			 'Cl': 35.5,
#			 'Na': 23,
#			 'Sn': 118.7}
#Nos pregunta los datos principales
print("Por favor, si tienes algun número decimal por . en vez de ,")
M = float(input("¿Molaridad?\n"))
ml = float(input("¿Cuantos mililitros?\n"))
r = int(input("¿Qué riqueza tiene?\n"))
d = float(input("¿Qué densidad tiene?\n"))
m_molecular = float(input("La masa molecular\n"))

def Calcular_cantidad(M,ml,r,d):
	ml_en_l = ml/1000
	n_moles = M*ml_en_l
	m = d*1000
	moles = m*(r/100)/m_molecular
	print("Moles necesarios:\n",moles)
	resultado = n_moles*1000/moles
	print("Necesitas: ",resultado,"ml")

Calcular_cantidad(M,ml,r,d)

