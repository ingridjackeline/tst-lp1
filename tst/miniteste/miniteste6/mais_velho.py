# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina, entre duas pessoas, quem é a mais velha

nome1 = input()
dia1 = int(input())
mes1 = int(input())
ano1 = int(input())
nome2 = input()
dia2 = int(input())
mes2 = int(input())
ano2 = int(input())

if ano1 != ano2:
	if ano1 < ano2:
		print(nome1)
	else:
		print(nome2)
		
elif mes1 != mes2:
	if mes1 < mes2:
		print(nome1)
	else:
		print(nome2)
		
elif dia1 != dia2:
	if dia1 < dia2:
		print(nome1)
	else:
		print(nome2)
		
else:
	print("nenhuma")								
