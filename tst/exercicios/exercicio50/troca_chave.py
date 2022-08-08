# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que recebe um dicionário e retorna o seu inverso

def troca_chave(dic):
	dic_inverso = {}
	
	for chave in dic:
		dic_inverso[dic[chave]] = chave
		
	return dic_inverso	
