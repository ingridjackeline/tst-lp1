# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime uma tabela dos quadrados dos valores entre X e Y 

x = int(input())
y = int(input())

if x <= y:
	for num in range(x, y + 1):
		quadrado = num ** 2 
		print(num, quadrado)
		
else: 
	print("---")		
