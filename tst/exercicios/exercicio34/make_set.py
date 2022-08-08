# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Função que recebe uma lista e a transforma em um conjunto

def make_set(lista):
	for i in range(len(lista) - 1, 0, -1):
		for p in range(i - 1, -1, -1):
			if lista[p] == lista[i]:
				lista.pop(i)
				break


l = [1, 2, 1]
make_set(l)
assert l == [1, 2]

l = [2, 2, 2]
make_set(l)
assert l == [2]
