# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a área de um cilindro 

import math 

print("Cálculo da Superfície de um Cilindro")
print("---")

diametro = float(input("Medida do diâmetro? "))
altura = float(input("Medida da altura? "))

raio = diametro / 2 
area = 2 * math.pi * raio * (raio + altura)

print("---")
print(f"Área calculada: {area:.2f}")
