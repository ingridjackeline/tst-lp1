# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que retorna a senha de um dado usuário

def senha(cadastro, usuario):
	for senha in cadastro:
		for nome in cadastro[senha]:
			if nome == usuario:
				return senha 
				
	return -1			
