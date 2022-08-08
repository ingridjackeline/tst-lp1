# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que determina a menor sequência de DNA e o seu tamanho 

sequencia1 = input()
sequencia2 = input()
sequencia3 = input()

if len(sequencia1) <= len(sequencia2) and len(sequencia1) <= len(sequencia3):
	print(f"{sequencia1} {len(sequencia1)}")
	
elif len(sequencia2) < len(sequencia1) and len(sequencia2) <= len(sequencia3):
	print(f"{sequencia2} {len(sequencia2)}")
		
else:
	print(f"{sequencia3} {len(sequencia3)}")	
	
