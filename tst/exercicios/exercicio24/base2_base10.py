# Ciência da Computação - UFCG
# Programação I
#
# Aluna: Ingrid Jackeline 
#
# Programa que converte um número binário em um número decimal

num_binario = input()

posicao_bits = []
num_decimal = 0

for expoente in range(len(num_binario) -1, -1, -1):
	potencia = 2 ** expoente
	posicao_bits.append(potencia)

for i in range(len(num_binario)):
	conversao_decimal = int(num_binario[i]) * posicao_bits[i]
	num_decimal += conversao_decimal
	print(f"{num_binario[i]} * {posicao_bits[i]} = {conversao_decimal}")
	
print(f"{num_binario}(2) = {num_decimal}(10)")	
