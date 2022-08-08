# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a soma dos últimos ímpares da sequência até um certo limite

num_itens = int(input())

if num_itens > 0:
	valor_limite = int(input())
	
	sequencia_impares = []
	soma_impares = 0
	
	for num in range(num_itens):
		valor = int(input())
		if valor % 2 != 0:
			sequencia_impares.append(valor)
			
	for i in range(len(sequencia_impares) - 1, -1, -1):
		if soma_impares + sequencia_impares[i] < valor_limite:
			soma_impares += sequencia_impares[i]
		else: break 
			
	print(soma_impares)		
