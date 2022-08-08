# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina quantas senhas numéricas tem dígitos adjacentes iguais

num_senhas = int(input())

digito_adjacente = ""
tem_adj_igual = False 
com_adj_igual = 0
sem_adj_igual = 0

for num in range(num_senhas):
	senha = input()
	
	for digito in senha:
		if digito == digito_adjacente:
			com_adj_igual += 1
			tem_adj_igual = True
			break
		else:
			digito_adjacente = digito	
				
	if tem_adj_igual == False:
		sem_adj_igual += 1	
	else:
		tem_adj_igual = False		
	
	digito_adjacente = ""
		
print(f"com: {com_adj_igual}")
print(f"sem: {sem_adj_igual}")			
