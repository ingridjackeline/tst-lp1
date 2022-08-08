# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina os valores de uma sequência que estão abaixo da média

sequencia = []
total = 0

while True:
	valor = input()
	
	if valor == "fim": break
	
	valor = int(valor)
	sequencia.append(valor)
	total += valor
		
media = total / len(sequencia)	

print(f"{media:.2f}")	
		
for i in range(len(sequencia)):
	if sequencia[i] < media:
		print(i + 1, sequencia[i])		
