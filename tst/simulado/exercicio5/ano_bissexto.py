# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que verifica se um ano é bissexto ou não 

ano = int(input())

if ano % 400 == 0:
	print(f"{ano} é bissexto")
elif ano % 4 == 0 and ano % 100 != 0:
	print(f"{ano} é bissexto")
else: 
	print(f"{ano} não é bissexto")		
