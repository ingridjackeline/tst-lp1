# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime a soma dos elementos lidos a cada K posições 

k = int(input())
n = int(input())

posicao = 0
soma = 0

for i in range(n):
	numero = int(input())
	
	if i == posicao:
		soma += numero
		posicao += k
		
print(f"Soma: {soma}.")
