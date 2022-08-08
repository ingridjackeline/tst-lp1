# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que consulta quantas casas há disponíveis à direita para a movimentação do jogador

def consulta_direita(labirinto):
	casas_livres = 0
	jogador = False
	
	for i in range(len(labirinto)):
		for j in range(len(labirinto[i])):
			if labirinto[i][j] == "*":
				jogador = True
			elif jogador == True:
				if labirinto[i][j] == " ":
					casas_livres += 1
				elif labirinto[i][j] == "P":
					return casas_livres 
		if jogador == True and j == len(labirinto[i]) - 1:
			return casas_livres								
