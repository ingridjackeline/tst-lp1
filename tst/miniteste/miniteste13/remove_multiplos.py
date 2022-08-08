# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que elimina todos os valores que forem múltiplos de um dado fator

def remove_multiplos(fator, numeros):
	quant_eliminados = 0
	for i in range(len(numeros) - 1, -1, -1):
		if numeros[i] % fator == 0:
			quant_eliminados += 1
			numeros.pop(i)
			
	return quant_eliminados		
	
	
numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(2, numeros) == 4
assert numeros == [5, 7, 3, 1]

numeros = [2, 4, 6, 5, 7, 3, 10, 1]
assert remove_multiplos(3, numeros) == 2
assert numeros == [2, 4, 5, 7, 10, 1]	
