# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que agrupa em um dicionário os números negativos e não negativos de uma lista

def agrupa_negativos(lista):
	nao_negativos = []
	negativos = []
	
	for numero in lista:
		if numero >= 0:
			nao_negativos.append(numero)
		else:
			negativos.append(numero)
			
	return {"nao-negativos":nao_negativos, "negativos":negativos}	
