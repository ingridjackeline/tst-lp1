# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que realiza operações em uma conta bancária 

nome_saldo = input().split()

nome_cliente = nome_saldo[0]
saldo_cliente = float(nome_saldo[1])

while True:
	codigo_valor = input().split()
	codigo_operacao = int(codigo_valor[0])
	
	if codigo_operacao == 1 or codigo_operacao == 2:
		valor = float(codigo_valor[1])
		if codigo_operacao == 1:
			saldo_cliente -= valor
		else:
			saldo_cliente += valor
			
	elif codigo_operacao == 3: break		

print(f"Saldo de R$ {saldo_cliente:.2f} na conta de {nome_cliente}")
