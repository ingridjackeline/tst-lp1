# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que retorna o número de palavras da lista que contém um dado caractere

def palavras_com_caractere(palavras, caractere):
	contem_caractere = 0
	
	for palavra in palavras:
		for letra in palavra:
			if letra == caractere:
				contem_caractere += 1
				break
			
	return contem_caractere
	
assert palavras_com_caractere(["casa", "carro", "teste"], "x") == 0
assert palavras_com_caractere(["casa", "carro", "teste"], "r") == 1
assert palavras_com_caractere(["casa", "carro", "teste"], "a") == 2				
