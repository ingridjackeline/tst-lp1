# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime todos os múltiplos de 5, pares e positivos menores que um dado limite 

numero_limite = int(input())

numero = 10

while numero < numero_limite:
	if numero % 5 == 0:
		print(numero)
		
	numero += 2
