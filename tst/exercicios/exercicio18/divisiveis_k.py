# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o número de inteiros divisíveis por K em uma dada sequência

k = int(input())
n = int(input())

quantidade = 0

for num in range(n):
	valor = int(input())
	if valor % k == 0:
		quantidade += 1
		
porcentagem = quantidade * 100 / n 

print(f"{quantidade} ({porcentagem:.1f}%)")		
