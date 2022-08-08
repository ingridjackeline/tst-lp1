# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que identifica se há vogais adjacentes em uma palavra

def tem_vogais_adjacentes(palavra):
	tem_vogais_adjacentes = "nao"
	
	for i in range(len(palavra) - 1):
		if palavra[i] in "aeiouAEIOU" and palavra[i + 1] in "aeiouAEIOU":
			tem_vogais_adjacentes = "sim"
			break
			
	return tem_vogais_adjacentes		
			
				
palavra = input()

print(tem_vogais_adjacentes(palavra))				
