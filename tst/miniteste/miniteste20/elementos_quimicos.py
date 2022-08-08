# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula a massa de várias moléculas

def massa_molecular(molecula):
	massas_atomicas = {"H": 1, "S": 32, "O": 16, "C": 12, "Ca": 40, "Na": 23, "P": 31}
	massa_molecular = 0
	massa_elemento = 0
	
	for i in range(len(molecula)):
		if not molecula[i].isdigit():
			for atomo in massas_atomicas:
				if atomo == molecula[i]:
					if i < len(molecula) - 1 and molecula[i + 1].isdigit():
						massa_elemento += massas_atomicas[atomo]
					else:
						massa_molecular += massas_atomicas[atomo]
		else:
			massa_elemento *= int(molecula[i])
			massa_molecular += massa_elemento
			massa_elemento = 0
			
	return massa_molecular		
					

massas_moleculares = []

while True:
	molecula = input().split()
	
	if molecula[0] == "fim": break
	
	massa = massa_molecular(molecula)
	massas_moleculares.append(massa)
	
for massa in massas_moleculares:
	print(massa)	
