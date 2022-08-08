# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que remove as palavras que possuem letras iguais consecutivas

def remove_consecutivas(lista):
	for i in range(len(lista) - 1, -1, -1):
		if lista[i].islower():
			palavra = lista[i]
		else:
			palavra = lista[i].lower() 
			
		for l in range(len(palavra) - 1):
			if palavra[l] == palavra[l + 1]:
				lista.pop(i)
				break
				
				
lista1 = ['arara', 'tv',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'tv',  'bacia']

lista1 = ['arara', 'arroba',   'bacia']
assert remove_consecutivas(lista1) == None
assert lista1 == ['arara', 'bacia']
