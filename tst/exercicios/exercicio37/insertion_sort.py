# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que ordena os elementos em ordem crescente, usando o algoritmo de ordenação por inserção

def insertion_sort(numeros):
	for i in range(1, len(numeros)):
		for p in range(i - 1, -1, -1):
			if numeros[p] > numeros[i]:
				numeros[p], numeros[i] = numeros[i], numeros[p]
				i = p 
			else: break	
				
				
numeros = [6, 3, 7, 9, 1, 0]
insertion_sort(numeros)
assert numeros == [0, 1, 3, 6, 7, 9]				
