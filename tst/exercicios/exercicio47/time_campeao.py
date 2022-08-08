# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna uma lista com o nome do time que possui mais pontos

def time_campeao(dados):
	maior_quant_pontos = 0
	time_campeao = []
	
	for time in dados:
		if dados[time][0] > maior_quant_pontos:
			maior_quant_pontos = dados[time][0]
			
	for time in dados:
		if dados[time][0] == maior_quant_pontos:
			time_campeao.append(time)
			
	return time_campeao		
