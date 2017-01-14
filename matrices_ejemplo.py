# -*- coding: utf-8 -*-

# La mas sencilla e intuitiva
# matriz = []
# for i in range(numero_filas):
#   matriz.append([])
#   for j in range(numero_columnas):
#      matriz[i].append(None)

print "Numero de filas"
numero_filas = input(":")
print "Numero de columnas"
numero_columnas = input(":")

# Menos intuitiva pero mas eficiente
# matriz = [None] * numero_filas
# for i in range(numero_filas):
#     matriz[i] = [None] * numero_columnas

# Versión mas compacta
matriz = [range(numero_columnas) for i in range(numero_filas)]

# Variación de la anterior
# matriz = [[None] * numero_columnas for i in range(numero_filas)]

print matriz