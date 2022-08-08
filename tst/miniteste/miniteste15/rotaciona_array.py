# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que faz uma rotação circular dos elementos do array uma posição à direita

def rotdir(array):
	for i in range(len(array) - 1, 0, -1):
		array[i], array[i - 1] = array[i - 1], array[i]
