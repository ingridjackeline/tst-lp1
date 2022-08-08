# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime os ímpares positivos menores que n 

n = int(input())

for num in range(n):
	if num % 2 != 0:
		print(num)
