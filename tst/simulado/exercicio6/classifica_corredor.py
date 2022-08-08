# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que classifica um corredor de acordo com a sua velocidade 

distancia = float(input())
tempo = float(input())

velocidade = distancia / tempo

if velocidade < 10:
	print(f"Velocidade: {velocidade:.1f}km/h. Corredor amador.")
elif velocidade >= 10 and velocidade <= 15:
	print(f"Velocidade: {velocidade:.1f}km/h. Corredor aspirante.")	
else: 
	print(f"Velocidade: {velocidade:.1f}km/h. Corredor profissional.")	
