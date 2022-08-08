# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna uma lista com a frequência de cada elemento na lista original

def get_frequencia(lista):
	lista_frequencia = [] 
	lista_elementos = []
	
	for i in range(len(lista)):
		esta_contido = False
		for elemento in lista_elementos:
			if elemento == lista[i]:
				esta_contido = True
				break
				
		if esta_contido == False:		
			frequencia = 1
			if i != len(lista) - 1:
				for p in range(i + 1, len(lista)):
					if lista[p] == lista[i]:
						frequencia += 1
			lista_frequencia.append(frequencia)
			lista_elementos.append(lista[i])	
				
	return lista_frequencia
		
assert get_frequencia(['b','b','c','b', 'a']) == [3,1,1]		
