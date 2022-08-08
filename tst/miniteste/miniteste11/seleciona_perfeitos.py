# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que retorna uma lista contendo os números perfeitos

def seleciona_perfeitos(lista):
	nums_perfeitos = []
	
	for num in lista:
		soma = 0
		for divisor in range(1, num):
			if num % divisor == 0:
				soma += divisor
		if soma == num:
			nums_perfeitos.append(num)	
						
	return nums_perfeitos			
			
lista = [3, 6, 9, 12, 15, 18, 19, 21, 28]
assert seleciona_perfeitos(lista) == [6, 28]
assert lista == [3, 6, 9, 12, 15, 18, 19, 21, 28]			
