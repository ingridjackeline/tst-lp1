# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna um valor booleano indicando se o roteiro de viagem pode ou não ser realizado

def eh_roteiro(iata, voos, roteiro_viagem):
	roteiro_viagem = roteiro_viagem.split("/")
	
	for i in range(len(roteiro_viagem) - 1):
		if iata[roteiro_viagem[i + 1]] not in voos[iata[roteiro_viagem[i]]]:
			return False
	
	return True		
