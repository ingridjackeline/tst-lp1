# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que identifica o maior fator primo, menor que 10, de um número 

numero = int(input())

if numero % 7 == 0:
	k = numero // 7
	print(f"7 * {k} = {numero}")
elif numero % 5 == 0:
	k = numero // 5 
	print(f"5 * {k} = {numero}")	
elif numero % 3 == 0:
	k = numero // 3
	print(f"3 * {k} = {numero}")
elif numero % 2 == 0:
	k = numero // 2
	print(f"2 * {k} = {numero}")		
else:
	print(f"{numero} não tem fatores primos menores que 10")
	
