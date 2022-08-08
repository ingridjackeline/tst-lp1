# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que determina a intersecção entre duas listas

def intersecao_listas(lista1, lista2):
	for i in range(len(lista1) - 1, -1, -1):
		intersecao = False
		
		for p in range(len(lista2)):
			if lista2[p] == lista1[i]:
				intersecao = True
				break
				
		if intersecao == False:
			lista1.pop(i)		
			
lista1 = [2, 1, 3, 4]
lista2 = [2]
intersecao_listas(lista1, lista2)
assert lista1 == [2]

lista1 = [1, 3, 4]
lista2 = [4, 3]
intersecao_listas(lista1, lista2)
assert lista1 == [3, 4]

lista1 = [2, 4, 1]
lista2 = [1, 3, 4]
intersecao_listas(lista1, lista2)
assert lista1 == [4, 1]			
