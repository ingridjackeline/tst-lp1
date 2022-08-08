# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a área de algumas figuras planas 

import math

tipo = input()

if tipo == "círculo" or tipo == "quadrado":
	raio_lado = float(input())
	if tipo == "círculo":
		area_circulo = math.pi * raio_lado ** 2
		print(f"Área do círculo: {area_circulo:.2f} (cm2)")
	else: 
		area_quadrado = raio_lado ** 2 
		print(f"Área do quadrado: {area_quadrado:.2f} (cm2)")
		
elif tipo == "retângulo" or tipo == "triângulo":
	base = float(input())
	altura = float(input())
	if tipo == "retângulo":
		area_retangulo = base * altura 
		print(f"Área do retângulo: {area_retangulo:.2f} (cm2)")
	else:
		area_triangulo = base * altura / 2 
		print(f"Área do triângulo: {area_triangulo:.2f} (cm2)")				
