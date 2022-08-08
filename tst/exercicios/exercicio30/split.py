# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que tokeniza uma string de acordo com um dado caractere delimitador

def split(frase, delimitador):
	token = ""
	lista_frase = []
	
	for caractere in frase:
		if caractere == delimitador:
			if token != "":
				lista_frase.append(token)
				token = ""
		else:
			token += caractere		
				
	if token != "":
		lista_frase.append(token)
		
	return lista_frase
	
assert split('um exemplo', ' ') == ['um','exemplo']
assert split('testando', 'a') == ['test', 'ndo']
