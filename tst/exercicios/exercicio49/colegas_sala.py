# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna uma lista com os colegas de sala do professor

def colegas_de_sala(salasprofs, professor):
	colegas_sala = []
	
	for nome in salasprofs:
		if nome != professor:
			if salasprofs[nome] == salasprofs[professor]:
				colegas_sala.append(nome)
			
	return colegas_sala
