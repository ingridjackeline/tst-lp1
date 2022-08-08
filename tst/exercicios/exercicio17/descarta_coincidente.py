# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que lê vários números e os seleciona de acordo com seus algarismos e suas respectivas posições

quantidade_num = int(input())

num_aceitos = []
num_descartados = []
descarta = False

for num in range(quantidade_num):
	numero = input()
	for i in range(len(numero)):
		if i == int(numero[i]):
			num_descartados.append(numero)
			descarta = True
			break
			
	if descarta == False:	
		num_aceitos.append(numero)		
	else:
		descarta = False
	
print("---")
print(f"{len(num_aceitos)} aceito(s)")

for num in num_aceitos:
	print(num)
	
print(f"{len(num_descartados)} descartado(s)")

for num in num_descartados:
	print(num)	
