# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que interage com o usuário do jogo de tiro ao alvo 

import math

num_disparos = 0
soma_distancias = 0

while True:
	posicao_tiro = input().split()
	
	x = float(posicao_tiro[0])
	y = float(posicao_tiro[1])
	distancia_tiro = math.sqrt(x ** 2 + y ** 2)
	
	if distancia_tiro > 200: break
	
	num_disparos += 1
	soma_distancias += distancia_tiro
	
	print(f"{distancia_tiro:.2f}cm")
	
distancia_media = soma_distancias / num_disparos
	
print("--")
print(f"num disparos: {num_disparos}")
print(f"distancia media: {distancia_media:.2f}cm")
