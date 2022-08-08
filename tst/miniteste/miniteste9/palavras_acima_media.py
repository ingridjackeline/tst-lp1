# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina quais palavras possuem um tamanho que está acima da média

sequencia_palavras = []
tamanho_palavras = 0

while True:
	palavra = input()
	
	if palavra == "fim": break
	
	sequencia_palavras.append(palavra)
	tamanho_palavras += len(palavra)
	
media_palavras = tamanho_palavras / len(sequencia_palavras)

print(f"{media_palavras:.2f}")	

for i in range(len(sequencia_palavras)):
	if len(sequencia_palavras[i]) > media_palavras:
		print(i + 1, sequencia_palavras[i])
