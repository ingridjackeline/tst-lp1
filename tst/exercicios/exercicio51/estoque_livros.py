# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna a quantidade de títulos que estão zerados no estoque de uma livraria

def ausentes(estoque):
	titulos_ausentes = 0
	
	for titulo in estoque:
		if estoque[titulo] == 0:
			titulos_ausentes += 1
			
	return titulos_ausentes	
