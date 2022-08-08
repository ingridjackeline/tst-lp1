# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que remove os dígitos repetidos de uma lista

def remove_repetidos(lista):
	for i in range(len(lista) - 1, 0, -1):
		for p in range(i - 1, -1, -1):
			if lista[p] == lista[i]:
				lista.pop(i)
				break
				
				
digitos = [1, 1, 2, 2, 5, 1]
assert remove_repetidos(digitos) == None
assert digitos == [1, 2, 5]

digitos = [1, 2, 1, 2, 1, 1]
assert remove_repetidos(digitos) == None
assert digitos == [1, 2]				
