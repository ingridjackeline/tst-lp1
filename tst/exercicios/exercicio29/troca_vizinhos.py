# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que altera as posições de pares de palavras vizinhas em uma dada sequência

def troca_vizinhos_condicional(seq):
	for i in range(len(seq)):
		if i % 2 == 1:
			if seq[i][0] < seq[i - 1][0]:
				palavra = seq[i - 1]
				seq[i - 1] = seq[i]
				seq[i] = palavra
				
# seq[i -1], seq[i] = seq[i], seq[i -1]

palavras = ["casa", "abacate", "boi", "casa", "jornal", "elo", "faca"]
troca_vizinhos_condicional(palavras)
assert palavras == ["abacate",  "casa", "boi", "casa", "elo", "jornal", "faca"]

palavras = ["elo", "diretor", "casa", "boi"]
troca_vizinhos_condicional(palavras)
assert palavras == ["diretor", "elo", "boi", "casa"]
