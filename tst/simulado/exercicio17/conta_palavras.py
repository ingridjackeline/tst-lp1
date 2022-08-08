# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna a quantidade de palavras com comprimento maior ou igual a k

def conta_palavras(k, palavras):
	palavras = palavras.split(":")
	quant_palavras = 0
	
	for palavra in palavras:
		if len(palavra) >= k:
			quant_palavras += 1
			
	return quant_palavras
