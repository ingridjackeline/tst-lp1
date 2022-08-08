# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que identifica dígitos pares coincidentes entre dois números

numero1 = str(int(input()))
numero2 = str(int(input()))

soma_digitos = 0

if len(numero1) == len(numero2):
	print("Dígitos coincidentes")
	
	for i in range(len(numero1)):
		if numero1[i] == numero2[i]:
			if int(numero1[i]) % 2 == 0:
				soma_digitos += int(numero1[i])
				print(f"{numero1[i]} na posição {i + 1}")
				
	print(f"Soma de dígitos coincidentes: {soma_digitos}")
