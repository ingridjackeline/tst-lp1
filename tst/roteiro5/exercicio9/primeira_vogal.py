# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime a primeira vogal de uma palavra 

palavra = input()

contador = 0

for i in range(len(palavra)):
	if palavra[i] in "aeiouAEIOU":
		contador += 1
		print(palavra[i])
		break 
		
if contador == 0:
	print("-")		
