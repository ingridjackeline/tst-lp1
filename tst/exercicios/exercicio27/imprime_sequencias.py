# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que seleciona as sequências em que mais da metade de seus números é maior do que um número alvo 

num_alvo = int(input())

conjunto_sequencias = []
posicao_sequencias = []
posicao = 0

while True:
	string_inteiros = input()
	
	if string_inteiros == "fim": break
	
	lista_inteiros = string_inteiros.split()
	nums_maiores = 0
	posicao += 1
	
	for num in lista_inteiros:
		if int(num) > num_alvo:
			nums_maiores += 1
			
	if nums_maiores > len(lista_inteiros) / 2:
		conjunto_sequencias.append(string_inteiros)
		posicao_sequencias.append(posicao)
	
for i in range(len(conjunto_sequencias)):
	print(f"sequencia {posicao_sequencias[i]}: {conjunto_sequencias[i]}")
