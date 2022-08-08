# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula os lucros mensais de uma empresa 

lucros = []

for num in range(12):
	receita, despesa = input().split()
	receita = float(receita)
	despesa = float(despesa)
	lucro = receita - despesa 
	lucros.append(lucro)
	
for lucro in lucros:
	print(f"{lucro:4.1f}")
