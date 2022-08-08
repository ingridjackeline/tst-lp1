# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime uma tabela de senos e cossenos 

import math

angulo = float(input())
salto = float(input())
linhas = int(input())

angulos = [angulo]
graus = angulo

for linha in range(linhas - 1):
	graus += salto 
	angulos.append(graus)	
	
print("|Angulo|   Seno|Cosseno|")	

for ang in angulos:
	radiano = math.radians(ang)
	seno = math.sin(radiano)
	cosseno = math.cos(radiano)
	
	print(f"|{ang:6}|{seno:7.5f}|{cosseno:7.5f}|")
