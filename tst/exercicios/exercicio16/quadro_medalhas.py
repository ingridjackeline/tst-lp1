# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que imprime o país melhor colocado no quadro de medalhas 

medalhas_brasil = input().split()
medalhas_italia = input().split()

ouro_brasil = 0
prata_brasil = 0
bronze_brasil = 0
ouro_italia = 0
prata_italia = 0
bronze_italia = 0

for i in range(len(medalhas_brasil)):
	if int(medalhas_brasil[i]) == 0:
		ouro_brasil += 1 
	elif int(medalhas_brasil[i]) == 1:
		prata_brasil += 1
	elif int(medalhas_brasil[i]) == 2:
		bronze_brasil += 1	
		
for i in range(len(medalhas_italia)):
	if int(medalhas_italia[i]) == 0:
		ouro_italia += 1 
	elif int(medalhas_italia[i]) == 1:
		prata_italia += 1
	elif int(medalhas_italia[i]) == 2:
		bronze_italia += 1		
		
if ouro_brasil != ouro_italia:
	if ouro_brasil > ouro_italia:
		print("brasil")
	else:
		print("italia")
		
elif prata_brasil != prata_italia:
	if prata_brasil > prata_italia:
		print("brasil")
	else:
		print("italia")
		
elif bronze_brasil !=  bronze_italia:
	if bronze_brasil > bronze_italia:
		print("brasil")
	else:
		print("italia")
		
else:
	print("empate")									
