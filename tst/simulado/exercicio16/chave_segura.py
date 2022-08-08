# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que verifica se uma chave é segura ou não 

chave = input()

num_vogais = 0
consecutivo = chave[0]
num_consecutivos = 0
i = 0

while True:
	if chave[i] in "aeiou":
		num_vogais += 1	
		
	if chave[i] == consecutivo:
		num_consecutivos += 1
	else:
		consecutivo = chave[i]
		num_consecutivos = 1	
			
	if num_vogais > 5:
		print("Chave insegura. 6 vogais.")
		break	
	elif num_consecutivos == 3:
		print("Chave insegura. 3 caracteres consecutivos iguais.")
		break	
		
	i += 1	
	
	if i == len(chave):
		break

if num_vogais <= 5 and num_consecutivos < 3:
	print("Chave segura!")
