# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que altera uma lista de chegada para dar prioridade aos menores de idade

def maiores_final(fila):
	m = 0
	for i in range(len(fila) - 1, -1, -1):
		if fila[i] >= 18:
			m += 1
			fila[i], fila[-m] = fila[-m], fila[i]
			
			
fila = [12, 21, 35, 8, 12, 15]
assert maiores_final(fila) == None
assert fila == [12, 12, 15, 8, 21, 35]			
