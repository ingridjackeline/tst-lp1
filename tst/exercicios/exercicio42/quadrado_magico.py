# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que recebe uma matriz e verifica se ela representa um quadrado mágico

def eh_quadrado_magico(matriz):
	if len(matriz) != len(matriz[0]):
		return False
		
	lista_elementos = []
	
	for linha in matriz:
		for elemento in linha:
			lista_elementos.append(elemento)
	for i in range(len(lista_elementos) - 1):
		for p in range(i + 1, len(lista_elementos)):
			if lista_elementos[i] == lista_elementos[p]:
				return False
							
	soma_elementos = 0
	soma_diagonal1 = 0
	soma_diagonal2 = 0
	
	for i in range(len(matriz)):
		soma_linha = 0
		soma_coluna = 0
		d = len(matriz) - 1 - i
		soma_diagonal1 += matriz[i][d]
		soma_diagonal2 += matriz[i][i]	
		
		for j in range(len(matriz[i])):
			soma_linha += matriz[i][j]
			soma_coluna += matriz[j][i]
			
		if i == 0:
			soma_elementos = soma_linha
		if soma_linha != soma_elementos or soma_coluna != soma_elementos:
			return False
		
	if soma_diagonal1 != soma_elementos or soma_diagonal2 != soma_elementos:
		return False
	else:
		return True			
