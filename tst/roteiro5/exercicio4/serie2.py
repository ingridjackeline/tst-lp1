# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime todos os números de uma sequência específica

lista = [302]

for lista[-1] in lista:
	num = lista[-1] - 3 
	lista.append(num)
	
	if num == -10:
		break	

for num in lista:
	print(num)
