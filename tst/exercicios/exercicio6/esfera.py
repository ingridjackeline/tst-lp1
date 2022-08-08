# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a área e o volume de uma esfera 

import math

raio = float(input())

area = 4 * math.pi * raio ** 2 
volume = (4 * math.pi * raio ** 3) / 3

print(f"{area:.4f}")
print(f"{volume:.4f}")
