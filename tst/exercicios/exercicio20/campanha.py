# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que faz um resumo da campanha do Campinense em um campeonato

vitoria = 0
empate = 0
derrota = 0
gols_pro = 0
gols_contra = 0
pontos_casa = 0
pontos_fora = 0

for num in range(10):
	resultado_jogo = input()
	
	if resultado_jogo[5] == "c":
		gols_pro += int(resultado_jogo[0])
		gols_contra += int(resultado_jogo[2])
		if resultado_jogo[0] > resultado_jogo[2]:
			vitoria += 1 
			pontos_casa += 3
		elif resultado_jogo[0] == resultado_jogo[2]:
			empate += 1
			pontos_casa += 1
		else:
			derrota += 1
			
	elif resultado_jogo[5] == "f":	
		gols_pro += int(resultado_jogo[2])
		gols_contra += int(resultado_jogo[0])
		if resultado_jogo[0] < resultado_jogo[2]:
			vitoria += 1 
			pontos_fora += 3
		elif resultado_jogo[0] == resultado_jogo[2]:
			empate += 1
			pontos_fora += 1
		else:
			derrota += 1	
			
total_pontos = pontos_casa + pontos_fora
saldo_gols = gols_pro - gols_contra
				
print(f"{vitoria}v, {empate}e, {derrota}d")
print(f"pontos: {total_pontos}")	
print(f"saldo: {saldo_gols} ({gols_pro} pro, {gols_contra} contra)")	
print(f"pontos em casa: {pontos_casa}")
print(f"pontos fora: {pontos_fora}")		
