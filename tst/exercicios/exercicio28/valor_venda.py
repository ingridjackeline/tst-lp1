# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que calcula o valor de venda de um produto

def calcula_venda(compra, ipi, iof, lucro):
	valor_final = compra + (ipi * compra) + (iof * compra) + (lucro * compra)
	return valor_final

while True:
	informs_produto = input()
	
	if informs_produto == "-": break
	
	lista_informs = informs_produto.split(",")
	lista_valores = []
	
	for inform in lista_informs:
		lista_valores.append(float(inform))
	
	valor_venda = calcula_venda(lista_valores[0], lista_valores[1], lista_valores[2], lista_valores[3])
	
	print(f"O valor de venda para este produto deve ser R$ {valor_venda:.2f}")
