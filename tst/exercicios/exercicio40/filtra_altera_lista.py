# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que remove os elementos da lista cujos índices não são divisíveis por um dado número

def filtra_altera_lista(num, lista):
	for i in range(len(lista) - 1, -1, -1):
		if i % num != 0:
			lista.pop(i)
